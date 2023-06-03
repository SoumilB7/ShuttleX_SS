import cv2
import numpy as np
import dlib


cap = cv2.VideoCapture("rtsp://172.17.231.93:8080/h264.sdp")

detector = dlib.get_frontal_face_detector()

while True:

	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector(gray)

	i = 0
	for face in faces:
		i = i+1
	print(f"Number of faces: {i}")

	cv2.imshow('frame', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
