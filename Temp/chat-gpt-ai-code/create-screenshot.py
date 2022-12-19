import pyautogui

# Get the dimensions of the screen
width, height = pyautogui.size()

# Capture the screen
screenshot = pyautogui.screenshot()

# Save the screenshot to a file
screenshot.save('screen.png')

# Share the file with others on the same network
# You can use a file-sharing service or send the file directly to the other devices using a Python script
