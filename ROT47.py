#!
import sys

arg_source   = str((sys.argv)[1])   # -f for filename.txt or -s for string
arg_input    = str((sys.argv)[2])   # filename.txt or string

def rot18(inString):
	start_ascii = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
	shift_ascii = start_ascii[47:]+start_ascii[:47]
	trans_Key = str.maketrans(start_ascii, shift_ascii)
	return inString.translate(trans_Key)

if arg_source == '-s':
	print(rot18(arg_input))
if arg_source == '-f':
	file = open(arg_input,'r')
	content = file.read()
	file.close()
	print(rot18(content))



