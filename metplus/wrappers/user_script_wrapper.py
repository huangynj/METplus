"""
Program Name: user_script_wrapper.py
Contact(s): George McCabe
Abstract: Parent class for wrappers that process groups of times
History Log:  Initial version
Usage:
Parameters: None
Input Files:
Output Files:
Condition codes: 0 for success, 1 for failure
"""

import os
from datetime import datetime

from ..util import met_util as util
from ..util import time_util
from . import RuntimeFreqWrapper
from ..util import do_string_sub

'''!@namespace UserScriptWrapper
@brief Parent class for wrappers that run over a grouping of times
@endcode
'''

class UserScriptWrapper(RuntimeFreqWrapper):
    def __init__(self, config, instance=None, config_overrides={}):
        self.app_name = "user_script"
        super().__init__(config,
                         instance=instance,
                         config_overrides=config_overrides)

    def create_c_dict(self):
        c_dict = super().create_c_dict()

        c_dict['COMMAND_TEMPLATE'] = (
            self.config.getraw('config',
                               'USER_SCRIPT_COMMAND')
        )
        if not c_dict['COMMAND_TEMPLATE']:
            self.log_error("Must supply a command to run with "
                           "USER_SCRIPT_COMMAND")

        c_dict['IS_MET_CMD'] = False
        c_dict['LOG_THE_OUTPUT'] = True

        return c_dict

    def get_command(self):
        """! Builds the command to run the MET application
           @rtype string
           @return Returns a MET command with arguments that you can run
        """
        return self.c_dict['COMMAND']

    def run_at_time(self, input_dict):
        """! Runs the command for a given run time. This function loops
              over the list of forecast leads and list of custom loops
              and runs once for each combination
              Args:
                @param input_dict dictionary containing time information
        """

        # loop of forecast leads and process each
        lead_seq = util.get_lead_sequence(self.config, input_dict)
        for lead in lead_seq:
            input_dict['lead'] = lead

            # set current lead time config and environment variables
            time_info = time_util.ti_calculate(input_dict)

            self.logger.info(
                f"Processing forecast lead {time_info['lead_string']}"
            )

            if util.skip_time(time_info, self.c_dict.get('SKIP_TIMES', {})):
                self.logger.debug('Skipping run time')
                continue

            # Run for given init/valid time and forecast lead combination
            self.run_at_time_once(time_info)

    def run_at_time_once(self, time_info):
        """! Process runtime and build command to run

             @param time_info dictionary containing time information
             @returns True if command was run successfully, False otherwise
        """
        success = True
        for custom_string in self.c_dict['CUSTOM_LOOP_LIST']:
            if custom_string:
                self.logger.info(f"Processing custom string: {custom_string}")

            time_info['custom'] = custom_string

            # if lead and either init or valid are set, compute other string sub
            if time_info.get('lead') != '*':
                if (time_info.get('init') != '*'
                        or time_info.get('valid') != '*'):
                    time_info = time_util.ti_calculate(time_info)

            self.set_environment_variables(time_info)

            # substitute values from dictionary into command
            self.c_dict['COMMAND'] = (
                do_string_sub(self.c_dict['COMMAND_TEMPLATE'],
                              **time_info)
            )

            # if command contains wildcard character, run in shell
            if '*' in self.c_dict['COMMAND']:
                self.c_dict['RUN_IN_SHELL'] = True

            # run command
            if not self.build():
                success = False

        return success