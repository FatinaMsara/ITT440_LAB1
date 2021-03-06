import socket
import sys
import time
import errno
import math
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server'))
    while True:
        option = s_sock.recv(2048)
        dec = option.decode()
        print("The option is", dec)
        if not option:
            break
        number = s_sock.recv(2048)
        inumber = int(number)
        print("The number is" , inumber)
        if (dec == '1'):
          result = math.log(inumber)
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for log operation:", result)
        elif (dec == '2'):
          result = math.sqrt(inumber)
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for square root operation:", result)
        elif (dec == '3'):
          result = math.exp(inumber)
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for exponential operation:", result)
        elif (dec == '4'):
          s_sock.close()
          print("Client has been disconnected.")
        else:
          print("Invalid option. Try again!")
          s_sock.close()
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()


            except socket.error:

                print('got a socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
           s.close()
