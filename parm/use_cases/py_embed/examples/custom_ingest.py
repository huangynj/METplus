# ExampleWrapper example

[config]
# Options are times, processes
# times = run all items in the PROCESS_LIST for a single initialization
# time, then repeat until all times have been evaluated.
# processes = run each item in the PROCESS_LIST for all times
#   specified, then repeat for the next item in the PROCESS_LIST.
LOOP_ORDER = times

# time looping - options are INIT, VALID, RETRO, and REALTIME
LOOP_BY = VALID

# Format of VALID_BEG and VALID_END
VALID_TIME_FMT = %Y%m%d%H

# Start time for METplus run
VALID_BEG = 2013022712

# End time for METplus run
VALID_END = 2013022712

# Increment between METplus runs in seconds. Must be >= 60
VALID_INCREMENT = 21600

# list of forecast leads to process
LEAD_SEQ = 0

# List of applications to run
PROCESS_LIST = CustomIngest

CUSTOM_INGEST_1_SCRIPT = {SCRIPTS_DIR}/read_NRL_binary.py {INPUT_BASE}/py_embed/trpres_sfc_0000.0_0000.0_glob360x181_{valid?fmt=%Y%m%d%H}_00000000_fcstfld
CUSTOM_INGEST_1_TYPE = NUMPY
CUSTOM_INGEST_1_OUTPUT_GRID = {INPUT_BASE}/fake/some/file/that/defines/output/grid.nc

CUSTOM_INGEST_2_SCRIPT = {SCRIPTS_DIR}/read_ECMWF_NC_2D.py {INPUT_BASE}/py_embed/NR2006.pl.1by1.6522.2006012806.nc TP_6h
CUSTOM_INGEST_2_TYPE = NUMPY
CUSTOM_INGEST_2_OUTPUT_GRID = {INPUT_BASE}/fake/some/file/that/defines/output/grid.nc

[dir]
SCRIPTS_DIR = {PARM_BASE}/use_cases/py_embed/scripts

[filename_templates]
CUSTOM_INGEST_1_OUTPUT_TEMPLATE = {OUTPUT_BASE}/py_embed/pres_sfc.nc
CUSTOM_INGEST_2_OUTPUT_TEMPLATE = {OUTPUT_BASE}/py_embed/tp_6h.nc