import serial
from time import sleep
import sys
###########################################################
from pykeyboard import PyKeyboard
###########################################################\

Linux = 1

COM = "/dev/ttyUSB0"# (Linux)
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(2)
print(ser.name)

'''
#check args
if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False
'''
###########################################################

# must be lower than 15 or update key_codes
numkeys = 9

keys = [False]*numkeys
keys_states = [False]*numkeys

# key_codes: letters range from: 0x41 - 0x5A
key_codes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
#0x4F = letter:  O
# B C D E F G H 
# 
#key_codes = [0x41,0x42,0x43,0x56,0x4E,0x28,0x26,0x4D,0x49,0x4A,0x4B,0x4C,0x4D,0x4E,0x4F]
# F10 - F24
#key_codes = [0x79,0x7A,0x7B,0x7C,0x7D,0x7E,0x7F,0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87]



def setvalues(l):
	for i in range(numkeys):
		value = l[i]		
		if (value != "1"):
			value = "0"
			l[i] = value
		keys[i] = value

def switch_key(i):
	if value == '1':
		PressKey(key_codes[i])
	else:
		ReleaseKey(key_codes[i])



def check(l):
	value = ""
	for i in range(numkeys):
		value = l[i]
		if value != keys[i]:
			keys[i] = value
			keys_states[i] = not keys_states[i]
		if keys_states[i]:
			send_key(i)

k = PyKeyboard()

def send_key(i):
    k.tap_key(key_codes[i])
    #pyautogui.keyDown(key_codes[i])
    #pyautogui.press(key_codes[i])
    #pyautogui.keyUp(key_codes[i])


def check2(l):
	value = ""
	for i in range(numkeys):
		if l[i] == "1":
			send_key(i)
	



while True:	
	val = str(ser.readline().decode('utf-8', errors='ignore').strip('\r\n'))#Capture serial output as a decoded string
	valL = val.split("/")
	check2(valL)	
	#print(keys,end=" :: ",flush = True)
	#print(valL,end=" --- ",flush = True)
	print(val, end="\r", flush=True)




