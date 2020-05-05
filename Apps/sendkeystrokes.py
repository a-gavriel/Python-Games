import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12



keys = {
    "0": 0x30,"1": 0x31,"2": 0x32,"3": 0x33,
    "4": 0x34,"5": 0x35,"6": 0x36,"7": 0x37,
    "8": 0x38,"9": 0x39,"a": 0x41,"b": 0x42,
    "c": 0x43,"d": 0x44,"e": 0x45,"f": 0x46,
    "g": 0x47,"h": 0x48,"i": 0x49,"j": 0x4A,
    "k": 0x4B,"l": 0x4C,"m": 0x4D,"n": 0x4E,
    "o": 0x4F,"p": 0x50,"q": 0x51,"r": 0x52,
    "s": 0x53,"t": 0x54,"u": 0x55,"v": 0x56,
    "w": 0x57,"x": 0x58,"y": 0x59,"z": 0x5A,
    " ": 0x20,
}





# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def AltTab():
    """Press Alt+Tab and hold Alt key for 2 seconds
    in order to see the overlay.
    """
    PressKey(VK_MENU)   # Alt
    PressKey(VK_TAB)    # Tab
    ReleaseKey(VK_TAB)  # Tab~
    time.sleep(2)
    ReleaseKey(VK_MENU) # Alt~


def Moveafk():
    print ('2 seconds remaining')
    time.sleep(1)
    print ('1 second remaining')
    time.sleep(1)
    while(1):
        PressKey(0x44) # D
        time.sleep(1)
        PressKey(0x41) # A  0x20
        time.sleep(1)
        PressKey(0x43) # A  0x20
        time.sleep(1)
        PressKey(0x55) # A  0x20
        time.sleep(1)
        ReleaseKey(0x44)
        ReleaseKey(0x41)
        ReleaseKey(0x55)
        ReleaseKey(0x43)
        time.sleep(1)

        PressKey(0x45) # E  0x1B
        time.sleep(1)
        PressKey(0x20) 
        time.sleep(1)
        ReleaseKey(0x20)
        ReleaseKey(0x45)


        PressKey(0x44) # D
        time.sleep(1)
        PressKey(0x41) # A  0x20
        time.sleep(1)
        PressKey(0x43) # A  0x20
        time.sleep(1)
        PressKey(0x54) # A  0x20
        time.sleep(1)
        ReleaseKey(0x44)
        ReleaseKey(0x41)
        ReleaseKey(0x54)
        ReleaseKey(0x43)
        time.sleep(1)

        PressKey(0x45) # E  0x1B
        time.sleep(1)
        PressKey(0x20) 
        time.sleep(1)
        ReleaseKey(0x20)
        ReleaseKey(0x45)

        PressKey(0x1B)
        ReleaseKey(0x1B)


        
def singlekey():
    print ('2 seconds remaining')
    time.sleep(1)
    print ('1 second remaining')
    time.sleep(1)
    while(1):
        PressKey(0x49)         # i
        ReleaseKey(0x49)
        time.sleep(0.7)

def Discord(x):
    print ('5 seconds remaining')
    time.sleep(5)
    print ('1 second remaining')
    time.sleep(1)
    for i in range(x):
        PressKey(0x44) # D
        PressKey(0x49) # I
        PressKey(0x53) # S
        PressKey(0x43) # C
        PressKey(0x4F) # O
        PressKey(0x52) # R
        PressKey(0x44) # D        
        PressKey(0x0D) # Enter
        #time.sleep(0.5)
    

def message(text, number):
    print ('2 seconds remaining')
    time.sleep(1)
    print ('1 second remaining')
    time.sleep(1)
    text = text.lower().replace("\\n","\n")
    for each in range(number):
        for letter in text:
            if letter == "\n":
                code = 0x0D
            else:
                code = keys.get(letter)
            PressKey(code)   
            ReleaseKey(code)
        time.sleep(0.0001)


msg = input("Write message to send: ")
if msg:
    amount = int(input("Enter amount of messages: "))
    message(msg,amount)
    
'''
codes:
https://docs.microsoft.com/en-us/windows/desktop/inputdev/virtual-key-codes
'''
#if __name__ == "__main__":
#    AltTab()
