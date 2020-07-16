from imutils import paths
import argparse
import cv2

import convolution
import clear_bg

if __name__ == "__main__":
  # construct the argument parse and parse the arguments
  print("[INFO] detecting possible blur regions...")
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--images", required=True,
    help="path to input directory of images")
  ap.add_argument("-t", "--threshold", type=float, default=100.0,
    help="focus measures that fall below this value will be considered 'blurry'")
  args = vars(ap.parse_args())

  for image_path in paths.list_images(args["images"]):
    image = cv2.imread(image_path)

    #We may need to clear some bgs in order get a better result
    masked_image = clear_bg.remove_bg(image)

    # Runs the convolution that runs the blur detection
    # Here we get the roi with the smaller value
    smaller_fm_roi = convolution.convole(masked_image, image)
    # show the rois that's possibly blurred
    cv2.imshow("Possibly blurry regions", smaller_fm_roi)
    key = cv2.waitKey(0)