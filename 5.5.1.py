import socket

s = socket.socket()

PORT = 8888
print("\nServer is listing on port :", PORT)

s.bind(('', PORT))

s.listen(10)

file = open("recv.txt", "wb")
print("Sended file name will be recv.txt at server side\n")

while True:

    conn, addr = s.accept()

    msg = "\nHi Client[IP address: "+ addr[0] + "]\nWelcome to Server\nFrom: Server\n"
    conn.send(msg.encode())

    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)

    file.close()
    print("File has been send successfully")

    conn.close()
    print("Server closed the connection\n")

    break
