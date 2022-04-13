from cvzone.HandTrackingModule import HandDetector
from screeninfo import get_monitors
import cv2
import numpy as np
import os
import time


class FPS:
    """
    Helps in finding Frames Per Second and display on an OpenCV Image
    """

    def __init__(self):
        self.pTime = time.time()

    def update(self, img=None, pos=(20, 50), color=(255, 0, 0), scale=3, thickness=3):
        cTime = time.time()
        try:
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            if img is None:
                return fps
            else:
                cv2.putText(img, f'FPS: {int(fps)}', pos, cv2.FONT_HERSHEY_PLAIN, scale, color, thickness)
                return fps, img
        except:
            return 0


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Size:
    def __init__(self, w, h):
        self.w = w
        self.h = h


class Component:
    def __init__(self, pos, size, parent=None):
        self.pos = pos
        self.size = size

    def focused(self, x, y):
        return self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height

    def enabled(self, x, y):
        return self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height


class Logo(Component):
    pass


class Header(Component):
    pass


class Body(Component):
    pass


class Container(Component):
    pass


class Table(Component):
    pass


class Row(Component):
    pass


class Column(Component):
    pass


class Cell(Component):
    pass


class Footer(Component):
    pass


class Button(Component):
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def click(self, img, value):
        self.border((255, 255, 255), img)
        self.text(value, img)

    def focused(self, x, y):
        return self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height


class Image:
    pass


class ImageButton(Button):
    pass


class Product:
    def __init__(self, id, type, slug, ean, title, descripton, small_image, ):
        pass


class CartItem(Button, Product):
    pass


class Cart:
    pass


gestureThreshold = 300
path_folder = "shop"

primary_monitor = {}
for m in get_monitors():
    print("Connected monitors {}".format(m))
    if m.is_primary:
        primary_monitor = m
        break

cap = cv2.VideoCapture(0)
cap.set(3, primary_monitor.width)
cap.set(4, primary_monitor.height)

frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
circleCenter = (round(frameWidth / 2), round(frameHeight / 2))

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Variables
product_images = []
product_image_index = 0
hs, ws = int(120 * 1.5), int(213 * 1.5)  # width and height of small image

# Get list of presentation images
path_images = sorted(os.listdir(path_folder), key=len)

print(f"{len(path_images)} products imported..")

fps_reader = FPS()

while cap.isOpened():
    # Get image frame
    success, img = cap.read()
    # check if frame grabbed successfully
    if success == False:
        continue

    fps, img = fps_reader.update(img)

    img = cv2.flip(img, 1)
    absolute_path_image = os.path.join(path_folder, path_images[product_image_index])
    imgCurrent = cv2.imread(absolute_path_image)

    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # Draw Gesture Threshold line
    scroll_x1, scroll_y1, scroll_x2, scroll_y2 = 0, gestureThreshold, primary_monitor.width, gestureThreshold
    cv2.line(img, (scroll_x1, scroll_y1), (scroll_x2, scroll_y2), (255, 100, 0), 10)

    if hands:  # If hand is detected

        landmarks = hands[0]['lmList']

        fingers = detector.fingersUp(hands[0])  # List of which fingers are up
        pointIndex = landmarks[8][0:2]
        middleIndex = landmarks[12][0:2]
        distance, _, img = detector.findDistance(pointIndex, middleIndex, img)

        if len(hands) == 1 and distance < 65:

            hold = 1
            print(f"fps = {fps}")
            hold += 1
        elif len(hands) == 2:
            print("Two hands alternative..")

    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws: w] = imgSmall

    cv2.imshow("Slides", imgCurrent)
    # cv2.imshow("Image", img)

    cv2.namedWindow("Slides", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("Slides", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
