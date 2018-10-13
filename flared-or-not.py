#!/usr/bin/python2.7

# import the necessary packages
import cv2
import argparse
from imutils import paths

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
                help="focus measures that fall below this value will be considered 'Not flared'")
args = vars(ap.parse_args())

#Load image
img = cv2.imread(args["image"])

#Compute mean brigtness
rgbmean = cv2.mean(cv2.mean(img))

#Print 1 if the image is 'flared' and 0 if not
if rgbmean[0] > args["threshold"]:
    #Flared
    print (1)
else:
    #Not flared
    print (0)

# Threshold for this set of images it's around 72
# ./flared-or-not.py -i ~/training-data/good-data -t 72