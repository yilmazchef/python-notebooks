import pyautogui
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def share_screen():
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot to a file
    screenshot.save('screen.png')

    # Serve the file as an image
    return send_file('screen.png', mimetype='image/png')

if __name__ == '__main__':
    # Run the web server on localhost
    app.run(host='localhost')
