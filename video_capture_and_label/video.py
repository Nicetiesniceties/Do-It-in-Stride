###############################################################################
#     This is an 30-minute code so sorry for the nastiness and nestedness.    #
###############################################################################
# import required libraries
import cv2
import time
import os
import time



cap = cv2.VideoCapture(0)


# Get video metadata
video_fps = cap.get(cv2.CAP_PROP_FPS),
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#fourcc = cv2.VideoWriter_fourcc(*'avc1')
#writer = cv2.VideoWriter('OUTPUT_PATH.mp4', apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
#                     fps=video_fps[0], frameSize=(int(width), int(height)))
writer = cv2.VideoWriter('test.mp4', apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                     fps=video_fps[0], frameSize=(int(width), int(height)))
Gesture_N = 46
GestureList = [
        "NormalWalking",
        "TapOuward",
        "TapInFrontOfTheOtherFoot",
        "TapInward",
        "BigStep", 
        "SmallStep",
        "ToeTapBehind",
        "ToeTapInFront",
        "TapWithHeel",
        "TapWithFootRotatedOutwards",
        "TapWithFootRotatedInwards",
        "Click",
        "KickInward",
        "KickOutward",
        "KickForward",
        "LiftInFront",
        "BendingBehind",
        "MidairRotationInwards",
        "MidairRotationOutwards",
        "DraggingInFront",
        "DraggingBehind",
        "Delay",
        "Rush"
    ]

gestureArray = [
        "0 12 14 4 17 16 6 3 2 10 1 8 15 21 7 5 19 13 20 18 11 9 22",
        "0 21 8 10 16 22 15 14 1 2 19 3 6 17 13 12 18 20 9 5 11 4 7",
        "0 6 20 10 12 19 9 4 17 18 16 21 13 14 5 3 15 8 7 2 1 11 22",
        "0 19 3 5 15 7 18 13 12 8 1 4 14 10 20 21 16 22 2 9 6 17 11",
        "0 8 10 15 6 2 9 7 3 20 12 1 14 4 18 19 11 16 21 5 17 22 13",
        "0 1 13 11 10 22 15 19 18 4 14 6 8 17 12 3 21 20 9 2 16 7 5",
        "0 2 22 17 15 10 13 21 6 9 19 18 4 8 20 11 14 16 12 3 7 5 1",
        "0 21 11 5 20 15 22 19 9 13 18 17 7 6 3 4 8 14 12 10 2 16 1",
        "0 22 13 7 3 9 4 10 2 6 11 20 1 17 15 18 21 14 12 8 19 5 16",
        "0 2 10 7 14 6 3 17 11 16 13 20 22 5 18 9 21 1 19 12 4 8 15",
        "0 3 17 7 5 13 8 10 9 22 2 6 14 19 11 20 16 21 18 12 1 4 15",
        "0 10 7 15 11 20 9 17 19 12 18 2 16 3 22 21 5 4 8 13 6 14 1",
        "0 7 13 1 18 12 19 2 8 15 17 9 22 16 20 6 3 11 5 21 4 14 10",
        "0 15 11 8 1 12 19 16 17 4 7 20 5 13 18 3 14 22 21 10 9 6 2",
        "0 4 13 6 3 19 17 8 2 12 15 14 20 18 9 11 7 21 5 10 22 16 1",
        "0 22 4 17 6 18 11 20 19 3 7 9 8 12 13 14 15 16 21 2 1 10 5",
        "0 13 7 19 15 1 4 8 18 22 6 16 3 9 5 11 20 2 10 21 12 14 17",
        "0 19 16 22 9 11 21 15 20 18 5 10 3 4 17 8 13 6 7 1 2 12 14",
        "0 11 14 7 12 2 13 5 19 6 3 20 8 22 15 17 16 4 9 21 18 1 10",
        "0 12 18 4 6 1 14 15 17 9 16 20 5 13 21 2 3 7 11 19 8 22 10",
        "0 1 10 22 15 7 13 19 11 16 17 2 12 21 5 6 4 20 9 3 18 14 8",
        "0 11 19 5 9 15 2 8 16 22 7 4 12 21 20 18 14 13 3 6 1 17 10",
        "0 18 11 19 9 17 20 13 22 5 1 16 14 8 21 7 4 6 10 15 2 12 3",
        "0 7 6 14 18 8 12 2 15 9 1 13 17 16 19 10 22 4 20 11 3 21 5",
        "0 5 6 2 3 15 21 1 7 19 17 8 11 13 22 14 4 18 16 10 12 20 9",
        "0 5 17 16 3 4 20 13 18 1 11 15 9 12 7 10 14 6 21 19 2 8 22",
        "0 7 6 12 4 20 3 16 2 21 10 5 14 1 15 18 17 9 19 11 13 8 22",
        "0 14 17 15 22 3 18 10 21 11 12 4 13 16 6 8 5 20 19 7 2 9 1",
        "0 21 14 9 4 2 16 10 15 3 8 13 1 11 22 12 6 18 17 20 7 19 5",
        "0 5 10 14 2 21 3 9 7 19 16 1 18 13 12 6 22 4 17 15 11 20 8"
    ]

footednessArray = [
        "0 0 0 1 0 1 0 1 0 1 0 1 1 0 1 0 0 1 1 0 0 1 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 0 1 0 0 1",
        "0 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 0 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 1 0 1 0 0 1 0 1",
        "0 0 1 0 0 1 0 1 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 0 1 0 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1",
        "0 0 1 0 1 0 0 1 1 0 0 1 0 1 0 1 1 0 1 0 0 1 1 0 1 0 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 1 0",
        "0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 1 0 0 1 0 1",
        "0 0 1 0 1 0 1 0 1 0 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 1 0 0 1 1 0 1 0 0 1 1 0 0 1 1 0 0 1 1 0",
        "0 0 1 0 1 0 1 0 0 1 0 1 1 0 1 0 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 0 0 1 1 0 0 1 0 1 1 0",
        "0 0 0 1 0 1 1 0 0 1 1 0 1 0 1 0 1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1 1 0 1 0",
        "0 0 1 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0 1 0 1 0 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 1 0 0 1 1 0 0 1",
        "0 0 1 0 1 0 0 1 1 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0 0 1 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 0 1",
        "0 0 1 0 0 1 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 1 0 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1",
        "0 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 0 1 1 0 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 1 0",
        "0 0 1 0 0 1 1 0 1 0 1 0 1 0 0 1 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 1 0 1 0",
        "0 0 0 1 0 1 0 1 1 0 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1",
        "0 0 0 1 0 1 0 1 0 1 1 0 0 1 1 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0 1 1 0 0 1 0 1 1 0 1 0 0 1 1 0",
        "0 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 0 1 0 1 0 1 0 1 0 1 1 0 1 0 1 0",
        "0 0 0 1 0 1 1 0 1 0 0 1 1 0 1 0 1 0 1 0 0 1 0 1 0 1 1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 0 1",
        "0 0 0 1 1 0 0 1 0 1 0 1 0 1 1 0 0 1 0 1 1 0 1 0 0 1 1 0 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 0 1 0",
        "0 0 1 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 0 0 1 0 1 0 1 0 1",
        "0 0 1 0 1 0 0 1 1 0 0 1 0 1 0 1 1 0 1 0 1 0 0 1 1 0 0 1 0 1 0 1 1 0 1 0 0 1 1 0 1 0 1 0 1 0",
        "0 0 1 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0 1 0 0 1 0 1 1 0 1 0 1 0 0 1 0 1",
        "0 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0 0 1 1 0 1 0 0 1 1 0 0 1 1 0 1 0",
        "0 0 1 0 1 0 1 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0",
        "0 0 0 1 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0",
        "0 0 1 0 1 0 0 1 1 0 1 0 1 0 1 0 1 0 0 1 1 0 0 1 1 0 0 1 1 0 1 0 0 1 1 0 1 0 1 0 1 0 0 1 0 1",
        "0 0 1 0 0 1 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 0 0 1 1 0 1 0 1 0 1 0 1 0",
        "0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1",
        "0 0 0 1 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 1 0 0 1 0 1 1 0 1 0 1 0 1 0 0 1 1 0 1 0 1 0 0 1 1 0",
        "0 0 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 0 1 1 0 1 0 1 0 1 0 0 1 1 0 0 1 1 0 0 1 0 1 1 0 0 1 1 0",
        "0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 1 0 1 0 0 1 0 1 0 1 0 1 1 0 1 0 1 0 0 1 1 0 0 1 0 1 0 1"
    ]


UserID = input("UserID:")
dirpath = "D:\Do it in Stride\VideoRecord"
dirpath = os.path.join(dirpath, UserID)
if(not os.path.exists(dirpath)):
    os.mkdir(dirpath)
UserID = int(UserID) - 1
GestureOrder = gestureArray[UserID].split(' ')
# print(GestureOrder)
FootOrder = footednessArray[UserID].split(' ')
# print(FootOrder)
recording_status = False

def create_pathname(condition_n, is_forth):
    gesture = GestureList[int(GestureOrder[condition_n // 2])]
    if(gesture == "NormalWalking"):
        foot = "bothfeet"
    else:
        foot = ("leftfoot" if FootOrder[condition_n] == "0" else "rightfoot")
    forth = ("forth" if is_forth == "y" else "back")
    timestamp = str(int(round(time.time() * 1000)))
    pathname = "p" + str(UserID) + "-" + gesture + "-" + foot + "-" + forth + "-" + timestamp + ".mp4"
    return pathname

# infinite loop
while True:
    
    ret, frame = cap.read()
    if not ret: break # break if cannot receive frame
    ## convert to grayscale
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    
    
    # do something with both frameA and frameB here
    #cv2.imshow("Output Frame1", frameA)
    #cv2.imshow("Output Frame2", frameB)
    # Show output window of stream1 and stream 2 seperately

    # Display the resulting frame    
    cv2.imshow('frame',frame)

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break

    if key == ord(" "):
        if recording_status == False:
            condition = int(input("please input the condition_N"))
            forth = input("going forth? [y/n]")

            filename = create_pathname(condition, forth)
            finalpath = os.path.join(dirpath, filename)
            writer = cv2.VideoWriter(finalpath, apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                     fps=video_fps[0], frameSize=(int(width), int(height)))
            recording_status = True
        else:
            recording_status = False

    if recording_status == True:
        # continue
        writer.write(frame) # write frame


## release and destroy windows
writer.release()
cap.release()
cv2.destroyAllWindows()

