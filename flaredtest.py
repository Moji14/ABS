#!/usr/bin/python2.7

# import the necessary packages
from imutils import paths
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
                help="focus measures that fall below this value will be considered 'Not flared'")
args = vars(ap.parse_args())

# loop over the input images
for imagePath in paths.list_images(args["images"]):
    img = cv2.imread(imagePath)

    # Scaling image to display it
    imgScale = 0.2  # W / width
    newX, newY = img.shape[1] * imgScale, img.shape[0] * imgScale
    newimg = cv2.resize(img, (int(newX), int(newY)))

    #Compute mean brigtness
    rgbmean = cv2.mean(cv2.mean(newimg))

    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    text = "Not Flared"
    if rgbmean[0] > args["threshold"]:
        text = "Flared"

    # show the image
    cv2.putText(newimg, "{}: {:.2f}".format(text, rgbmean[0]), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", newimg)

    key = cv2.waitKey(0)
# Threshold for this set of images it's around 72
# ./flared-or-not.py -i ~/training-data/good-data -t 72
