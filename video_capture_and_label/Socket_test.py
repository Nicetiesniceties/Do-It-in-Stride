import socket
 
backlog = 1
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(backlog)
try:
    print ("is waiting")
    client, address = s.accept()

    while 1:
        data = client.recv(size)
        if data:
            print (data)

except:
    print("closing socket")
    client.close()
    s.close()