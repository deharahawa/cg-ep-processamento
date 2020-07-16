import argparse
import cv2

# Uses laplacian covariance
def var_of_laplacian (image):
  # Based on the https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/ tutorial
  return cv2.Laplacian(image, cv2.CV_64F).var()


# to find blurred regions
def find_blur(roi):
  # Based on https://stackoverflow.com/questions/57233870/blur-detection-of-image-using-opencv, https://stackoverflow.com/questions/7765810/is-there-a-way-to-detect-if-an-image-is-blurry and https://stackoverflow.com/questions/19443908/detecting-how-blurred-an-image-is

  gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  fm = var_of_laplacian(gray)
  return fm

    