"""
PlotDataPlane: Python Embedding Input
=====================================

met_tool_wrapper/PlotDataPlane/PlotDataPlane_python_embedding.conf

"""
##############################################################################
# Scientific Objective
# --------------------
#
# Generate a postscript image to test if the input data can be read by the MET
# tools.

##############################################################################
# Datasets
# --------
#
# | **Input:** Sample Python Embedding script/file
#
# | **Location:** All of the input data required for this use case can be found in the met_test sample data tarball. Click here to the METplus releases page and download sample data for the appropriate release: https://github.com/dtcenter/METplus/releases
# | This tarball should be unpacked into the directory that you will set the value of INPUT_BASE. See 'Running METplus' section for more information.
#
# | **Data Source:** Unknown
# |

##############################################################################
# METplus Components
# ------------------
#
# This use case utilizes the METplus PlotDataPlane wrapper to generate a
# command to run the MET tool PlotDataPlane if all required files are found.

##############################################################################
# METplus Workflow
# ----------------
#
# PlotDataPlane is the only tool called in this example.
# It processes the following run time:
#
# | **Valid:** 2005-08-07 12Z
# |

##############################################################################
# METplus Configuration
# ---------------------
#
# METplus first loads all of the configuration files found in parm/metplus_config,
# then it loads any configuration files passed to METplus via the command line
# with the -c option, i.e. -c parm/use_cases/met_tool_wrapper/PlotDataPlane/PlotDataPlane_python_embedding.conf
#
# .. highlight:: bash
# .. literalinclude:: ../../../../parm/use_cases/met_tool_wrapper/PlotDataPlane/PlotDataPlane_python_embedding.conf

##############################################################################
# MET Configuration
# -----------------
#
# This tool does not use a MET configuration file.
#

##############################################################################
# Python Embedding
# ----------------
#
# This use case calls a Python script to read the input data.
# The Python script is stored in the MET repository: /path/to/MET/installation/share/met/python/read_ascii_numpy.py
#
# `read_ascii_numpy.py <https://github.com/dtcenter/MET/blob/develop/met/scripts/python/read_ascii_numpy.py>`_

##############################################################################
# Running METplus
# ---------------
#
# This use case can be run two ways:
#
# 1) Passing in PlotDataPlane_python_embedding.conf then a user-specific system configuration file::
#
#        run_metplus.py -c /path/to/METplus/parm/use_cases/met_tool_wrapper/PlotDataPlane/PlotDataPlane_python_embedding.conf -c /path/to/user_system.conf
#
# 2) Modifying the configurations in parm/metplus_config, then passing in PlotDataPlane_python_embedding.conf::
#
#        run_metplus.py -c /path/to/METplus/parm/use_cases/met_tool_wrapper/PlotDataPlane/PlotDataPlane_python_embedding.conf
#
# The former method is recommended. Whether you add them to a user-specific configuration file or modify the metplus_config files, the following variables must be set correctly:
#
# * **INPUT_BASE** - Path to directory where sample data tarballs are unpacked (See Datasets section to obtain tarballs). This is not required to run METplus, but it is required to run the examples in parm/use_cases
# * **OUTPUT_BASE** - Path where METplus output will be written. This must be in a location where you have write permissions
# * **MET_INSTALL_DIR** - Path to location where MET is installed locally
#
# Example User Configuration File::
#
#   [dir]
#   INPUT_BASE = /path/to/sample/input/data
#   OUTPUT_BASE = /path/to/output/dir
#   MET_INSTALL_DIR = /path/to/met-X.Y 
#
# **NOTE:** All of these items must be found under the [dir] section.
#

##############################################################################
# Expected Output
# ---------------
#
# A successful run will output the following both to the screen and to the logfile::
#
#   INFO: METplus has successfully finished running.
#
# Refer to the value set for **OUTPUT_BASE** to find where the output data was generated.
# Output for this use case will be found in met_tool_wrapper/plot_data_plane
# (relative to **OUTPUT_BASE**)
# and will contain the following file:
#
# * py_embed_fcst.ps

##############################################################################
# Keywords
# --------
#
# .. note::
#
#   * PlotDataPlaneToolUseCase
#   * PythonEmbeddingFileUseCase
#
#   Navigate to the :ref:`quick-search` page to discover other similar use cases.
#
#
#
# sphinx_gallery_thumbnail_path = '_static/met_tool_wrapper-PlotDataPlane.png'
#
