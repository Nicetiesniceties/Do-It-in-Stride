import cv2
import time
import os

def parse_filename(filename):
    filename = filename.split(".")[0]
    filename = filename.split("-")
    return filename

userid = input("UserID:")
dirpath = "D:\Do it in Stride\VideoRecord"
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

video_list.sort(key = lambda x: int(x[-1]), reverse = True)
for i in video_list:
    cap = cv2.VideoCapture(os.path.join(userdirpath, i[0]))
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    print(video_fps)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    print(i[0])
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("frame initalization fail")
            break
        cv2.imshow('frame', frame)
        key = cv2.waitKey(int(20)) & 0xFF
        # check for 'q' key-press
        if key == ord("q"):
            #if 'q' key-pressed break out
            break
        if key == ord("c"):
            #if 'q' key-pressed break out
            quit();
        if key == ord("g"):
            print("time at: ", cap.get(cv2.CAP_PROP_POS_MSEC));

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