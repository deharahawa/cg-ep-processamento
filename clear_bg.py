import cv2
import numpy as np

# CÓDIGO DE https://stackoverflow.com/questions/29313667/how-do-i-remove-the-background-from-this-kind-of-image
# Acabamos nao implementando essa parte por conta do tempo e dificuldade em ajustar os parâmetro sendo que o foco era detectar os rostos com blur.

def remove_bg(image): 
  #== Parameters 
  BLUR = 21
  CANNY_THRESH_1 = 10
  CANNY_THRESH_2 = 200
  MASK_DILATE_ITER = 10
  MASK_ERODE_ITER = 10
  MASK_COLOR = (0.0,0.0,0.0) # In BGR format


  #== Processing 

  #-- Read image 
  gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

  #-- Edge detection 
  edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
  edges = cv2.dilate(edges, None)
  edges = cv2.erode(edges, None)

  #-- Find contours in edges, sort by area 
  contour_info = []
  contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
  for c in contours:
      contour_info.append((
          c,
          cv2.isContourConvex(c),
          cv2.contourArea(c),
      ))
  contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
  max_contour = contour_info[0]

  #-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
  # Mask is black, polygon is white
  mask = np.zeros(edges.shape)
  cv2.fillConvexPoly(mask, max_contour[0], (255))

  #-- Smooth mask, then blur it 
  mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
  mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
  mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
  mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask

  #-- Blend masked img into MASK_COLOR background 
  mask_stack = mask_stack.astype('float32') / 255.0          # Use float matrices, 
  img = image.astype('float32') / 255.0 

  masked = (mask_stack * img) + ((1-mask_stack) * MASK_COLOR) # Blend
  masked = (masked * 255).astype('uint8')                     # Convert back to 8-bit 

  return masked