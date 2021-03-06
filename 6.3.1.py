import socket
import math
ClientSocket = socket.socket()
host = '192.168.56.101'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    print("Option:   1-Logarithmic(Log)      2-Square Root    3-Exponential    4-Exit\n")
    option = input('Enter Your Option: ')
    ClientSocket.send(str.encode(option))
    number = input('Enter number: ')
    ClientSocket.send(str.encode(number))
    if (option == '1'):
      print("Log Operation")
    elif (option == '2'):
      print("Square Root Operation")
    elif (option == '3'):
      print("Exponential Operation")
    elif (option == '4'):
      print("Bye!")
      ClientSocket.close()
    else:
      print("Invalid option. Try again!")
    result = ClientSocket.recv(1024)
    print("Result:",result.decode('utf-8'))
ClientSocket.close()
