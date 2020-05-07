import argparse
import cv2

# Uses laplacian covariance
def var_of_laplacian (image):
  return cv2.Laplacian(image, cv2.CV_64F).var()


# to find blurred regions
def find_blur(roi):
  gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  fm = var_of_laplacian(gray)
  return fm

    