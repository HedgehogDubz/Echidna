import re
import os
import pyttsx3

import ctypes
import win32api, win32con


def RunCommands(input_string):
    print("RUNNING")
    commands = SplitCommands(input_string)
    for command in commands:
        if ":" in command:
            split_command = command.split(":")
            command_type = split_command[0]
            command_descriptor = split_command[1]
            RunDescriptorCommands(command_type, command_descriptor)
        else:
            RunTypeCommands(command)
    

def SplitCommands(input_string):
    # Use regular expression to find all the substrings within square brackets
    matches = re.findall(r'\[([^\]]+)\]', input_string)
    
    return matches

# Example usage:
input_string = "[ABC][DEF][GHI]"
result_array = SplitCommands(input_string)
print(result_array)

def RunDescriptorCommands(command_type, command_descriptor):
    match command_type:
        case "say":
            Speak(command_descriptor)
        case "search":
            SearchInternet(command_descriptor)
            print("SEARCHING FOR: " + command_descriptor)

    return

def RunTypeCommands(command):
    match command:
        case "turnoff":
            turn_off_monitor()
        case "turnon":
            turn_on_monitor()

    return

def SearchInternet(search_term):
    os.system("start \"\" https://www.google.com/search?q=" + search_term.replace(" ", "+"))

def Speak(words):
    tts_engine = pyttsx3.init()
    tts_engine.say(words)
    tts_engine.runAndWait()
    tts_engine.stop()

# Define necessary constants
HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MONITOR_OFF = 2
MONITOR_ON = -1

# Get user32.dll
user32 = ctypes.WinDLL('user32')

def turn_off_monitor():
    user32.SendNotifyMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)

# Function to turn on the monitor
def turn_on_monitor():
    user32.SendNotifyMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)
    move_cursor()

def move_cursor():
    x, y = (0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
