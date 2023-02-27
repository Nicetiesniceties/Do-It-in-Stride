import cv2
import time
import os
import socket
import threading
import multiprocessing

backlog = 1
size = 1024
# create the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a local address
server_socket.bind(('127.0.0.1', 12345))

# listen for incoming connections
server_socket.listen(1)

# flag to indicate whether the threads should stop
recording_status = False

# read in video from webcam devices
cap1 = cv2.VideoCapture(3)
cap2 = cv2.VideoCapture(2)

# Get video metadata
video_fps1 = cap1.get(cv2.CAP_PROP_FPS),
height1 = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
width1 = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)

video_fps2 = cap2.get(cv2.CAP_PROP_FPS),
height2 = cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)
width2 = cap2.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc(*'avc1')
writer1 = cv2.VideoWriter('test1.mp4', apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                     fps=video_fps1[0], frameSize=(int(width1), int(height1)))
writer2 = cv2.VideoWriter('test2.mp4', apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                     fps=video_fps2[0], frameSize=(int(width2), int(height2)))

#create media data folder and setting user id
UserID = input("UserID:")
dirpath = "D:\Do it in Stride\VideoRecord"
dirpath = os.path.join(dirpath, UserID)
if(not os.path.exists(dirpath)):
    os.mkdir(dirpath)

print ("is waiting")
def recording_video(filepath1, filepath2):
    global recording_status
    print("starting recording ...")
    writer1 = cv2.VideoWriter(filepath1, apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                    fps=video_fps1[0], frameSize=(int(width1), int(height1)))
    writer2 = cv2.VideoWriter(filepath2, apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                    fps=video_fps2[0], frameSize=(int(width2), int(height2)))
    while True:
        # read device frame
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1: 
            print("frame1 initalization fail")
            break # break if not receiving from device
        if not ret2: 
            print("frame2 initalization fail")
            break
        cv2.imshow('frame1',frame1)
        cv2.imshow('frame2',frame2)
        key = cv2.waitKey(1) & 0xFF
        # check for 'q' key-press
        if key == ord("q"):
            #if 'q' key-pressed break out
            break
        #print("Bobobo")
        # write the command to the file
        writer1.write(frame1)
        writer2.write(frame2)
        # check if the command is the stop command
        if recording_status == False:
            break
    return

client_socket, client_address = server_socket.accept()
while True:
    # accept incoming connections
    
    # start a new thread to handle the connection
    data = client_socket.recv(size)
    if data:
        # process the incoming data
        print(f"Received data: {data.decode()}")
        if str(data) == "STOP":
            print("closing main process ...")
            recording_status = False
            sys.exit()
        else: 
            data = str(data)
            data = data[1:].strip('\'')
            isstart = data.split(" ")[0]
            data = data.split(" ")[1]
            print(data, isstart)
            if isstart == "start":
                    filename1 = "cam1-" + str(data) + ".mp4"
                    filename2 = "cam2-" + str(data) + ".mp4"
                    finalpath1 = os.path.join(dirpath, filename1)
                    finalpath2 = os.path.join(dirpath, filename2)
                    print(finalpath1, finalpath2)
                    recording_status = True
                    t = threading.Thread(target=recording_video, args=(finalpath1, finalpath2))
                    t.start()
            elif isstart == "stop":
                print("stop recording ...")
                recording_status = False
    # t = threading.Thread(target=receive_command, args=(client_socket,))
    # t.start()
 
