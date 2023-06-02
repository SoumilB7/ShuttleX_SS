# Import required libraries
import cv2
import numpy as np
import dlib


# Connects to your computer's default camera
cap = cv2.VideoCapture("rtsp://172.17.231.93:8080/h264.sdp")


# Detect the coordinates
detector = dlib.get_frontal_face_detector()


# Capture frames continuously
while True:

	# Capture frame-by-frame
	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)

	# RGB to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector(gray)

	# Iterator to count faces
	i = 0
	for face in faces:
		i = i+1
	print(f"Number of faces: {i}")

	# Display the resulting frame
	cv2.imshow('frame', frame)
	# This command let's us quit with the "q" button on a keyboard.
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# Release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
