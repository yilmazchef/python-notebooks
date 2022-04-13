import numpy as np
import cv2


class Button:

    def __init__(self, pos=(0, 0), width=100, height=200, value="Button", click_event=print):
        self.click_event = click_event
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def focused(self, x, y):
        return self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height

    def click(self, action):
        self.click_event = action

    def draw(self, img):
        self.border((255, 255, 255), img)
        self.text(self.value, img)

    def background(self, rgb, img):
        # for the background calculator
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), rgb, cv2.FILLED)

    def border(self, rgb, img):
        # for the border calculator
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), rgb, 3)

    def text(self, value, img):
        self.value = value
        cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255),
                    3)

    def text_hover(self, value, img):
        self.value = value
        cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 50), cv2.FONT_HERSHEY_PLAIN, 6, (255, 255, 255),
                    3)

    def move(self, pos, img):
        self.pos = pos
        self.border((255, 255, 255), img)
        self.text(self.value, img)


class ImageButton(Button):
    def __init__(self, pos=(0, 0), width=200, height=100, value="Image Button", click_event=None):
        super().__init__(pos, width, height, value, click_event)

    def draw(self, img):
        # percent by which the image is resized
        scale_percent = 50
        # calculate the 50 percent of original dimensions
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        # dsize
        dsize = (width, height)
        # resize image
        output = cv2.resize(img, dsize)
        return output

