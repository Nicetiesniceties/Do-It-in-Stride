import cv2
import time
import os
import socket
import threading
import multiprocessing
import keyboard

backlog = 1
size = 1024
# create the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a local address
server_socket.bind(('0.0.0.0', 12345))

# listen for incoming connections
server_socket.listen(1)


print ("is waiting")

client_socket, client_address = server_socket.accept()
client_socket.send(("aaa").encode())
while True:
    # accept incoming connections
    
    # start a new thread to handle the connection
    # data = client_socket.recv(size)
    # if data:
    #     # process the incoming data
    #     print(f"Received data: {data.decode()}")


    if keyboard.is_pressed(' '):
        #client_socket.send(("Message received at " + str(time.ctime(time.time()))).encode())
        print('You Pressed A Key!')
    button = keyboard.read_key()
    if button == "f":
        client_socket.send("Click".encode())
    elif button == "w":
        client_socket.send("Normal Walking".encode())
    elif button == "r":
        client_socket.send("BendingBehind".encode())
    elif button == "j":
        client_socket.send("Big Step".encode())
    elif button == "s":
        client_socket.send("ToeTapBehind".encode())
    elif button == "x":
        client_socket.send("Delay".encode())
    elif button == " ":
        client_socket.send("LiftInFront".encode())
    elif button == "p":
        client_socket.send("Stop!")
    elif button == "d":
        client_socket.send("RightBigStep".encode())
    elif button == "a":
        client_socket.send("LeftBigStep".encode())
    elif button == "c":
        client_socket.send("RightHeelTap".encode())
    elif button == "z":
        client_socket.send("LeftHeelTap".encode())
    elif button == "e":
        client_socket.send("RightClick".encode())
    elif button == "q":
        client_socket.send("LeftClick".encode())
    elif button == "b":
        client_socket.send("Call".encode())
    time.sleep(0.2)
    
 
'''
1709200114024, I, TrackerL, 0, 0, 0, 0, 0, 0
1709200114024, I, TrackerR, 0, 0, 0, 0, 0, 0
1709200114024, I, TrackerH, 0, 0, 0, 0, 0, 0
1709200114024, I, FootL, 0, 0, 0, 0, 0, 0
1709200114024, I, FootR, 0, 0, 0, 0, 0, 0
1709200114024, I, Head, 0, 0, 0, 0, 0, 0
'''