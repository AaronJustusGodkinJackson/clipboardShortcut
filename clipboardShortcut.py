#################################
# Program Name: clipboardShortcut
# Author: Aaron Godkin-Jackson
# Date: October 31st, 2020
# Description:
# - Takes whatever is on clipboard, cuts it into
#   an array of lines, and copies a line to clipboard
#   whenever you use the sohrtcut, so you don't need to manually
#   highlight the text
#######################################
import pyperclip
import keyboard
import time

clipboardData = pyperclip.paste()

linesToPaste = clipboardData.splitlines()

print(linesToPaste)

keyboard.wait('shift')
for line in linesToPaste:
    keyboard.write(line)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
