#!
import sys

arg_source   = str((sys.argv)[1])   # -f for filename.txt or -s for string
arg_input    = str((sys.argv)[2])   # filename.txt or string

def rot18(inString):
	start_Lower = "abcdefghijklmnopqrstuvwxyz"
	shift_Lower = start_Lower[13:]+start_Lower[:13]
	trans_Key = str.maketrans(start_Lower, shift_Lower)

	start_Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	shift_Upper = start_Upper[13:]+start_Upper[:13]
	trans_Key.update(str.maketrans(start_Upper, shift_Upper))

	return inString.translate(trans_Key)

if arg_source == '-s':
	print(rot18(arg_input))
if arg_source == '-f':
	file = open(arg_input,'r')
	content = file.read()
	file.close()
	print(rot18(content))



