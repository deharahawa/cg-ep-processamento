import numpy as np
import cv2

def anonymize_face_simple(image,factor=3.0):
	(h,w) = image.shape[:2]
	kW = int(w/factor)
	kH = int(h/factor)

	if kW % 2 == 0:
		kW -= 1

	if kH % 2 == 0:
		kH -= 1

	return cv2.GaussianBlur(image,(kW,kH),0)