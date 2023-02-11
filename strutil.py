#!/usr/bin/env python

#
#############################################################################
#
# strutil - String utility functions
# Copyright (C) 2015, testcams.com
#
# This module is licensed under GPL v3: http://www.gnu.org/licenses/gpl-3.0.html
#
#############################################################################
#

from __future__ import print_function
from __future__ import division
import six
from six.moves import xrange
import struct
from applog import *

def hexByte(value):
	return "0x{:02x}".format(value)
def hexShort(value):
	return "0x{:04x}".format(value)
def hexWord(value):
	return "0x{:08x}".format(value)

def hexByteFromData(data):
	(byte,)=struct.unpack('B',data[:1])
	return hexByte(byte)
def hexShortFromData(data):
	(short,)=struct.unpack('H',data[:2])
	return hexShort(short)	
def hexWordFromData(data):
	(word,)=struct.unpack('I',data[:4])
	return hexWord(word)	

#
# Generates string containing hex dump of a bytearray. Format is:
#
# bytesPerField=1:
#
# 	<offset>: xx xx xx xx xx xx xx xx - xx xx xx xx xx xx xx xx yyyyyyyy - yyyyyyyy
#
# bytesPerField=2:
#
#	<offset>: xxxx xxxx xxxx xxxx - xxxx xxxx xxxx xxx yyyyyyyy - yyyyyyyy
#
# bytesPerField=4:
#
#	<offset>: xxxxxxxx xxxxxxxx - xxxxxxxx xxxxxxx yyyyyyyy - yyyyyyyy
#
# Where 'xx' are the hex values of each byte/halfword/word and 'y' is
# the ASCII character equivalent ('.' for each non-printable ASCII value <32 or >127)
#
def hexdump(data, bytesPerField=1, includeASCII=1):
	bytesPerFieldToUnpackStr = { 1 : 'B', 2 : 'H', 4 : 'I', 8 : 'Q' }
	strHexDump=''
	if bytesPerField not in bytesPerFieldToUnpackStr:
		applog_w("hexdump: bytesPerField invalid. must be 1, 2, 4, or 8")
		return strHexDump
	if (len(data) % bytesPerField) != 0:
		applog_w("hexdump: size of data (0x{:04x}) is not a multiple of bytesPerField ({:d})".format(len(data), bytesPerField))
		return strHexDump
	for offset in xrange(0,len(data),bytesPerField):
		offsetThisFieldInLine = (offset % 16)	# byte offset into data for this field of current line
		endingOffsetThisFieldInLine = offsetThisFieldInLine + bytesPerField		
		if (offsetThisFieldInLine == 0):
			strHexDump += "{:04x}: ".format(offset)
		(thisField,) = struct.unpack(bytesPerFieldToUnpackStr[bytesPerField], data[offset:offset+bytesPerField])
		strHexDump += "{:0{:d}x} ".format(thisField, bytesPerField*2)		# (value,width) - width: bytes=2, halfwords=4, words=8
		if (endingOffsetThisFieldInLine == 8):
			strHexDump += "- "
		if (endingOffsetThisFieldInLine == 16 or (offset==len(data)-1)):
			# just processed 16 bytes of line or have reached final byte
			# of buffer (partial last line). Add ASCII representation
			# of hex values on this line.
			bIsFinalLine = (offset == len(data)-1)
			if includeASCII:
				if (endingOffsetThisFieldInLine < 16):
					# final line is a partial line. pad with spaces to
					# fill out area that would normally contain hex
					# values before start ASCII dump seciton
					fieldsNotPrintedInFinalLine = (16-endingOffsetThisFieldInLine) * bytesPerField
					charactersPerFieldIncludingSpace = bytesPerField*2 + 1
					strHexDump += " " * (fieldsNotPrintedInFinalLine*charactersPerFieldIncludingSpace) # add spaces for each missing field				
					if (endingOffsetThisFieldInLine < 8):
						strHexDump += "  "								# add spaces for missing middle separator
				for asciiOffset in range(offsetThisFieldInLine+1):
					(thisByte,) = struct.unpack('B', data[offset-offsetThisFieldInLine+asciiOffset:offset-offsetThisFieldInLine+asciiOffset+1])
					if (thisByte >= 32 and thisByte <= 127):
						strHexDump += six.unichr(thisByte)
					else:
						strHexDump += "."
					if (asciiOffset == 7):
						strHexDump += " - "
			if not bIsFinalLine:	# don't put newline after final line
				strHexDump += "\n"
	return strHexDump
		
