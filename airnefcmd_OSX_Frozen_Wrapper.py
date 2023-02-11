#!/usr/bin/env python

#
#############################################################################
#
# airnefcmd_OSX_Frozen_Wrapper.py - Wrapper around airnefcmd.py for use
# by the frozon airnef.py under OSX. This is a hack to work around the
# inability of a Python app running in an OSX bundle to launch a terminal
# app with parameters.
#
# Copyright (C) 2015, testcams.com
#
# This module is licensed under GPL v3: http://www.gnu.org/licenses/gpl-3.0.html
#
#############################################################################
#

from __future__ import print_function
from __future__ import division
import strutil
import time
import sys
import os
import errno
import airnefcmd

def createHackFileForAirnefCommunication(filename, data=None):
	fo = open(filename, "w")
	if data:
		fo.write(data)
	fo.close()

def deleteFileIgnoreErrors(filename):
    try:
        os.remove(filename)
    except:
        pass

#
# program entry point
#	
if __name__ == "__main__":
	
	appDir = os.path.dirname(os.path.realpath(sys.argv[0]))
	appDataDir = os.path.join(appDir, "appdata")

	FILENAME_CMD_OPTS		= os.path.join(appDataDir, "airnefcmd-osxfrozen-cmdopts")
	FILENAME_NOTIFY_START	= os.path.join(appDataDir, "airnefcmd-osxfrozen-notifystart")
	FILENAME_NOTIFY_DONE	= os.path.join(appDataDir, "airnefcmd-osxfrozen-notifydone")

	fo = open(FILENAME_CMD_OPTS, 'r')
	cmdArgs = fo.read().split('\n')
	fo.close()
	if cmdArgs[len(cmdArgs)-1] == '':
		cmdArgs.pop()
	sys.argv = [os.path.join(appDir, './airnefcmd.py')] + cmdArgs

	createHackFileForAirnefCommunication(FILENAME_NOTIFY_START, str(os.getpid()))
	_errno = 0
	try:
		_errno = airnefcmd.main()
	except:
		print("exception")
	print("airnefcmd.main() returned/exited") # debug-debug

	createHackFileForAirnefCommunication(FILENAME_NOTIFY_DONE, data=str(_errno))
