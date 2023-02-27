import cv2
import time
import os
import socket
import threading
import multiprocessing

# flag to indicate whether the threads should stop
recording_status = False

# read in video from webcam devices
cap1 = cv2.VideoCapture(3)


# Get video metadata
video_fps1 = cap1.get(cv2.CAP_PROP_FPS),
height1 = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
width1 = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)


#create media data folder and setting user id

print ("is waiting")
def recording_video():
    global recording_status
    print("starting recording ...")
    while True:
        # read device frame
        ret1, frame1 = cap1.read()

        if not ret1: 
            print("frame1 initalization fail")
            break # break if not receiving from device

        cv2.imshow('frame1',frame1)

        key = cv2.waitKey(1) & 0xFF
        # check for 'q' key-press
        if key == ord("q"):
            #if 'q' key-pressed break out
            break

    return

recording_video()