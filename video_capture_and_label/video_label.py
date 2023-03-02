import cv2
import time
import os
import pandas as pd

def parse_filename(filename):
    filename = filename.split(".")[0]
    filename = filename.split("-")
    return filename

def write_gesture_data_to_csv(timestamp_data):
    df = pd.DataFrame(timestamp_data)
    df.to_csv(str(userid) + "_gesture_stride_timestamp_" + name, mode='a', index = False)

def remove_duplicate(gesture_data):
    i = 0
    while i < len(gesture_data):
        if(i < 0): i = 0
        if(i + 1 < len(gesture_data)):
            if(gesture_data[i][1] == gesture_data[i + 1][1]
               and gesture_data[i][2] == gesture_data[i + 1][2]
               and gesture_data[i][3] == gesture_data[i + 1][3]
               and gesture_data[i][4] == gesture_data[i + 1][4]
               and gesture_data[i][5] == gesture_data[i + 1][5]
               and int(gesture_data[i][6]) < int(gesture_data[i + 1][6])):
                #print("remove", gesture_data[i][6], "due to", gesture_data[i + 1][6])
                gesture_data.pop(i)
                i -= 1
        i += 1
    return gesture_data

def record_gesture_timestamp(df, gesture_info, first_or_second, timestamp):
    gesture = gesture_info[3]
    foot = gesture_info[4]
    direction = gesture_info[5].strip("direction")
    camera = gesture_info[1]
    first_second = first_or_second
    timestamp = int(gesture_info[6]) + int(timestamp)
    df = pd.concat([df, pd.DataFrame([[gesture, foot, direction, camera, first_second, timestamp]], columns=["gesture", "foot", "direction", "camera", "first/second", "timestamp"])])
    #pd.DataFrame([[gesture, foot, direction, camera, first_second, timestamp]], columns=["gesture", "foot", "direction", "camera", "first/second", "timestamp"])
    print("gesture: ", gesture, "foot: ", foot, "direction: ", direction, "camera: ", camera, "first/second: ", first_second, "timestamp: ", timestamp)
    return df



name = input("Name (CY/DK/RY):")
if name not in ["CY", "DK", "RY"]:
    print("Invalid name, please try again!")
    exit()
userid = input("UserID:")

# change this to your own directory
dirpath = "D:\Do it in Stride\VideoRecord"


# read the video list and remove the duplicate
userdirpath = os.path.join(dirpath, userid)
video_list = []
if(not os.path.exists(userdirpath)):
    print("Data not exist!")
else:
    for root, dirs, files in os.walk(userdirpath):
        for file in files:
            if file.endswith(".mp4"):
                video_list.append([file] + parse_filename(file))
                #print(video_list[-1])
#print(video_list[0:5][0])
video_list = remove_duplicate(video_list)
print("video_list length: ", len(video_list), "this should be 180")
#print(video_list[0:5][0])
video_list.sort(key = lambda x: int(x[-1]), reverse = True)
#print(video_list[0:5][0])
#cam1-p3-BendingBehind-leftfoot-RecordingBack-1676407703513.mp4


# construct the final gesture timestamp data
df = pd.DataFrame(columns=["gesture", "foot", "direction", "camera", "first/second", "timestamp"])

i = 0
while i < len(video_list):
    if(i < 0): i = 0
    cap = cv2.VideoCapture(os.path.join(userdirpath, video_list[i][0]))
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    # print(video_fps)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    print("video #" + str(i), video_list[i][2], video_list[i][1], video_list[i][3], video_list[i][4], video_list[i][5].strip("Recording"))
    print(video_list[i][0])
    while True:
        ret, frame = cap.read()
        if not ret:
            #print("frame initalization fail")
            break
        # rotate frame by 90 degree
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # put text on frame
        cv2.putText(frame, video_list[i][3], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, video_list[i][4], (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(int(20)) & 0xFF
        # check for 'q' key-press
        if key == ord("d"):
            #skip video
            break
        if key == ord("a"):
            #previous video
            i -= 2
            break
        if key == ord("r"):
            #replay video
            i -= 1
            break
        if key == ord("q"):
            #if 'q' key-pressed save progress and quit
            print(df)
            write_gesture_data_to_csv(df);
            quit();
        if key == 32: 
            # spacebar for pause
            cv2.waitKey(-1)
        if key == ord("f"):
            #record first gesture
            #print("time at: ", int(cap.get(cv2.CAP_PROP_POS_MSEC)));
            df = record_gesture_timestamp(df, video_list[i], "first", cap.get(cv2.CAP_PROP_POS_MSEC))
        
        if key == ord("g"):
            #record second gesture
            #print("time at: ", int(cap.get(cv2.CAP_PROP_POS_MSEC)));
            df = record_gesture_timestamp(df, video_list[i], "second", cap.get(cv2.CAP_PROP_POS_MSEC))
    i += 1
        


# for i in video_list:
#     print(i[-1])


'''
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
'''