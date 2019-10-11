# Reading an image file
import argparse

import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help='Path to load image')
ap.add_argument("-s", "--save_path", required=True, help='Path to save image')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

if image is not None:
    print("width: {}".format(image.shape[1]))
    print("height: {}".format(image.shape[0]))
    print("channels: {}".format(image.shape[2]))

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.imwrite(args["save_path"], image)
    print("New image saved at path: {}".format(args["save_path"]))
else:
    print("Image not found at path")