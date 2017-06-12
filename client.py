# EE450 programming assignment 3
# Jiayi Zhang 3032914272

import socket
import string
import random

def GenMsg(size, chars = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

TCP_IP = '127.0.0.1'
# ID = raw_input('Input the client number: ')

TCP_PORT = 5005
buffer_size = 1024
# for i  in range(4):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))

message = GenMsg(random.randint(2000,1000000),)

# message = GenMsg(5500,)

s.send(message)

# data = s.recv(buffer_size)

# print("Received echo: %s" % data)

s.close()