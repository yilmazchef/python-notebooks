# Snake game on AR

import math
import random
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector


class Board:
    def __init__(self, path_food):
        self.points = []  # all points of the snake
        self.lengths = []  # distance between each point
        self.current_length = 0  # total length of the snake
        self.allowed_length = 150  # total allowed Length
        self.previous_head_position = 0, 0  # previous head point



        self.imgFood = cv2.imread(path_food, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomize_food_location()

        self.score = 0
        self.game_over = False

    def randomize_food_location(self):
        self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

    def update(self, img_main, current_head):

        if self.game_over:
            cvzone.putTextRect(img_main, "Game Over", [300, 400],
                               scale=7, thickness=5, offset=20)
            cvzone.putTextRect(img_main, f'Your Score: {self.score}', [300, 550],
                               scale=7, thickness=5, offset=20)
        else:
            px, py = self.previous_head_position
            cx, cy = current_head

            self.points.append([cx, cy])
            distance = math.hypot(cx - px, cy - py)
            self.lengths.append(distance)
            self.current_length += distance
            self.previous_head_position = cx, cy

            # Length Reduction
            if self.current_length > self.allowed_length:
                for i, length in enumerate(self.lengths):
                    self.current_length -= length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.current_length < self.allowed_length:
                        break

            # Check if snake ate the Food
            rx, ry = self.foodPoint
            if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                    ry - self.hFood // 2 < cy < ry + self.hFood // 2:
                self.randomize_food_location()
                self.allowed_length += 50
                self.score += 1

            # Draw Snake
            if self.points:
                for i, point in enumerate(self.points):
                    if i != 0:
                        cv2.line(img_main, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                cv2.circle(img_main, self.points[-1], 20, (0, 255, 0), cv2.FILLED)

            # Draw Food
            img_main = cvzone.overlayPNG(img_main, self.imgFood,
                                         (rx - self.wFood // 2, ry - self.hFood // 2))

            cvzone.putTextRect(img_main, f'Score: {self.score}', [50, 80],
                               scale=3, thickness=3, offset=10)

            # Check for Collision
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img_main, [pts], False, (0, 255, 0), 3)
            min_distance = cv2.pointPolygonTest(pts, (cx, cy), True)
            cvzone.putTextRect(img_main, f'Distance: {min_distance}', [600, 700], scale=2, thickness=2, offset=4)

        return img_main


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

game = Board("snake/pony.png")

while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        landmarks = hands[0]['lmList']
        point_index = landmarks[8][0:2]
        img = game.update(img, point_index)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        game.game_over = False
    elif key == ord('q'):
        game.game_over = True
        exit(-1)
