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
    if button == "a":
        client_socket.send("Click".encode())
        print("a")
    elif button == "c":
        client_socket.send("Normal Walking".encode())
        print("c")
    elif button == "d":
        client_socket.send("BendingBehind".encode())
        print("c")
    elif button == "f":
        client_socket.send("Big Step".encode())
        print("c")
    elif button == "g":
        client_socket.send("ToeTapBehind".encode())
        print("c")
    elif button == "h":
        client_socket.send("Delay".encode())
        print("c")
    elif button == "b":
        client_socket.send("Stop!")
        print("b")
    time.sleep(0.2)
    
 
'''
1709200114024, I, TrackerL, 0, 0, 0, 0, 0, 0
1709200114024, I, TrackerR, 0, 0, 0, 0, 0, 0
1709200114024, I, TrackerH, 0, 0, 0, 0, 0, 0
1709200114024, I, FootL, 0, 0, 0, 0, 0, 0
1709200114024, I, FootR, 0, 0, 0, 0, 0, 0
1709200114024, I, Head, 0, 0, 0, 0, 0, 0
'''