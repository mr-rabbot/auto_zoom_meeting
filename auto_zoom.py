import pyautogui as p
import time

# Meeting id number
MEETING_ID = '123456789'

# Name used to join the meeting
# Set to None if you can use your default Name
# Otherwise, change the value below
MY_NAME = 'YALU'

# Password used to join the meeting
# Set to None if the meeting doesn't require a password
# Otherwise, change the value below
PASSWORD = 'password'

# Open menu
p.press('win', interval=0.5)

# Search Zoom
p.typewrite('zoom', interval=0.1)
p.press('shift') # In case it is using Chinese input
p.press('enter')

# Opening Zoom
time.sleep(2)

# Click Join
x, y, width, height = p.locateOnScreen('join_button.png')
x += width / 2
y += height / 2
p.click(x, y)

# Open login dialog
time.sleep(1)

# Input meeting ID
p.typewrite(MEETING_ID, interval=0.1)

# Input new name if provided
if MY_NAME:
    # Go to the name input field
    p.press('tab')
    p.press('tab')
    # Delete default name
    p.hotkey('ctrl', 'a')
    p.hotkey('del')
    time.sleep(1)
    # Use new name
    p.press('shift') # In case it is using Chinese input
    p.typewrite(MY_NAME, interval=0.1)

p.press('enter')

time.sleep(2)

# Input password if needed
if PASSWORD:
    p.typewrite(PASSWORD, interval=0.1)

p.press('enter')
