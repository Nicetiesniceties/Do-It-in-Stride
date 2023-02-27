# import required libraries
import cv2
import time
import os
import time

import socket
import select

backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind(('127.0.0.1', 12345))
s.listen(backlog)


cap = cv2.VideoCapture(0)
inputs = [s]


# Get video metadata
video_fps = cap.get(cv2.CAP_PROP_FPS),
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc(*'avc1')
writer = cv2.VideoWriter('OUTPUT_PATH.mp4', apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                    fps=video_fps[0], frameSize=(int(width), int(height)))
writer = cv2.VideoWriter('test.mp4', apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                     fps=video_fps[0], frameSize=(int(width), int(height)))

UserID = input("UserID:")
dirpath = "D:\Do it in Stride\VideoRecord"
dirpath = os.path.join(dirpath, UserID)
if(not os.path.exists(dirpath)):
    os.mkdir(dirpath)

recording_status = False
print ("is waiting")


# infinite loop
while True:
    # use the select function to monitor the inputs for incoming data
    readable, _, _ = select.select(inputs, [], [], 0.5)


    
        
        
    ret, frame = cap.read()
    # print(frame)
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
    if recording_status == True:
        # continue
        writer.write(frame) # write frame
    for i in readable:
        # if the socket is the server socket, it means there is a new connection
        if i == s:
            client_socket, client_address = s.accept()
            # add the new socket to the list of inputs to be monitored
            inputs.append(client_socket)
        else:
            # if it's a client socket, it means there is incoming data
            try:
                data = i.recv(1024)
                if data:
                    # process the incoming data
                    print(f"Received data: {data.decode()}")
                    if recording_status == False:
                        data = str(data)
                        data = data[1:].strip('\'')
                        filename = str(data) + ".mp4"
                        finalpath = os.path.join(dirpath, filename)
                        print(finalpath)
                        writer = cv2.VideoWriter(finalpath, apiPreference=0, fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                                fps=video_fps[0], frameSize=(int(width), int(height)))
                        recording_status = True
                        print("starting recording ...")
                    else:
                        print("stop recording ...")
                        recording_status = False
                else:
                    # if there is no data, it means the connection has been closed
                    inputs.remove(i)
                    i.close()
            except socket.error:
                # handle any errors that occur
                inputs.remove(i)
                i.close()


