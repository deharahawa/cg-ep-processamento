from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

import blur_detection

# Runs a convolution through the
# image to find the region
# args: image in RGB
def convole (masked_image, original_image):
  # Get the image dimension to run the convolution
  (iH, iW) = masked_image.shape[:2]

  # The pad will take kW based on the image iW
  kW = int(iW / 5)
  kH = int(iH / 2)
  
  # Round it to pad
  padW = (kW - 1) // 2
  padH = (kH - 1) // 2
  # Create border to don't reduce the image
  # masked_image = cv2.copyMakeBorder(masked_image, padH, padH , padW, padW, cv2.BORDER_REPLICATE)
  
  # original_image = cv2.copyMakeBorder(original_image, padH, padH , padW, padW, cv2.BORDER_REPLICATE)
  # Crete empty image
  smaller_fm = 3000

  for y in np.arange(padH, iH + padH):
    for x in np.arange(padW, iW + padW):
      roi = masked_image[y - padH:y + padH + 1, x - padW:x + padW + 1]
      

      # Here we shall check the laplacian
      roi_fm = blur_detection.find_blur(roi)
      # print(roi_fm)
      
      if(roi_fm < 300 and roi_fm > 200):
        if(roi_fm < smaller_fm):
          # print(roi_fm)
          # always save the smaller roi
          smaller_fm = roi_fm
          # cv2.imshow('img', roi)                                   # Display
          # cv2.waitKey(0)
          # paint rectangles in the possibilities
          cv2.rectangle(original_image, (x - padW, y - padH), (x + padW + 1, y + padH + 1), (0, 255, 0), 2)

  return original_image
