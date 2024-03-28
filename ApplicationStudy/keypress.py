import keyboard
if keyboard.is_pressed(' '):
    client_socket.send(("Message received at " + str(time.ctime(time.time()))).encode())
    print('You Pressed A Key!')
while True:
    print(keyboard.read_key())
    if keyboard.read_key() == "a":
        print("a")