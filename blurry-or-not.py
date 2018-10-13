#!/usr/bin/python2.7

# import the necessary packages
import argparse
import cv2

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
                help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and compute the
# focus measure of the image using the Variance of Laplacian method
fm = variance_of_laplacian(cv2.cvtColor(cv2.imread(args["image"]), cv2.COLOR_BGR2GRAY))

# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < args["threshold"]:
    #Blurry
    result = 1
else:
    #Not Blurry
    result = 0
print result

# Threshold for this set of images it's around 700
#./blurry-or-not.py -i ~/training-data/blurry-data/20170502T171526_G0094538.JPG -t 700