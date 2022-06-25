import socket
import sys

s = socket.socket()

PORT = 8888

s.connect(('192.168.56.101', PORT))

print("\nWhat file do you want to send?: ")
filename = input("Enter filename: ")
print("Filename: " + filename)

# send file sample.txt
file = open("valul.txt", "rb")
SendData = file.read(1024)


while SendData:
    print("\nBelow message is received from server:-", s.recv(1024).decode("utf-8"))
    #send the content of sample.txt to server
    s.send(SendData)
    SendData = file.read(1024)

s.close()
