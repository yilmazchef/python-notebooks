# importing libraries
import cv2
import numpy as np
import pprint

# TODO: skip forward and backwards will be added.
# feature 01: with keyboard
# feature 02: with hand gestures (left hand raised backwards, right hand raised forward, both hands raised stop etc.)

# loading video gfg
source = input("Source: ")
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(source)

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)

# Check if camera opened successfully
if (cap.isOpened() == False):
	print("Error opening video file")

# Read until video is completed
while(cap.isOpened()):

	# Capture frame-by-frame
	ret, frame = cap.read()
	if ret == True:

		# Display the resulting frame
		cv2.imshow('Frame', frame)

		key = cv2.waitKey(1)
		
		# Press Q on keyboard to exit
		if cv2.waitKey(25) & 0xFF == ord('q'):
			# When everything done, release
			# the video capture object
			cap.release()
			# Closes all the frames
			cv2.destroyAllWindows()
			break

		# 'p' to stop
		elif key == ord('p') or key == ord('P'):
			key = cv2.waitKey()

		# 's' to save
		elif key == ord('s') or key == ord('S'):
			# Save the frame
			cv2.imwrite("frame.jpg", frame)
			print("Saved")


	# Break the loop
	else:
		break


# test video path
# C:\Users\intec\Videos\Recordings\Hackathon\Hackathon Intec Vision.mp4

