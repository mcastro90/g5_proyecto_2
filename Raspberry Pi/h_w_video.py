from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
vs = cv2.VideoCapture(args["video"])

_, frame = vs.read()

(w,h,c) = frame.shape

img = imutils.resize(frame,width=500)

print("original width and height")
print(w,h)
print("resized values h, w" )
print(img.shape)
