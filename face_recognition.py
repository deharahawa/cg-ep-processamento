import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')

image = cv2.imread("Images/test2.jpg")

while(True):

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
	for (x, y, w, h) in faces:
		print (x, y, w, h)
		roi_gray = gray[y:y+h, x:x+w] 
		roi_color = image[y:y+h, x:x+w]

		#Drawing the rectangle
		color = (0, 0, 255) #BGR
		stroke = 1
		xEnd = x + w
		yEnd = y + h 
		cv2.rectangle(image, (x,y), (xEnd, yEnd), color, stroke)

	#Display the resulting image
	cv2.imshow('image', image)
	cv2.waitKey(0)
	break

#When all its done
cv2.destroyAllWindows()
