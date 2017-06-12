# EE450 programming assignment 3
# Jiayi Zhang 3032914272

import socket
import locale
import select


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

locale.setlocale(locale.LC_ALL,'en_US')
buffer_size = 1000

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

sock.bind((TCP_IP, TCP_PORT))

print("Wait for connection...")

sock.listen(5)

ID = 1
total_bytes = []
clients = []
inputs = [sock]

while True:

	[rlist, wlist, xlist] = select.select(inputs, [], [])
	
	for r in rlist:
		if r is sock:
			conn, addr = sock.accept()
			inputs.append(conn)
			clients.append(conn)
			print ('\nConnected to address as client %d: %s: %d\n' % (ID, addr[0],addr[1]))
			ID += 1
			total_bytes.append(0)

		else:
			client_id = clients.index(r)
			data = r.recv(buffer_size)
			# if not data:
			# 	break
			if data:
				bytes = len(data)
				total_bytes[client_id] += bytes
				bytes = locale.format('%d', bytes, grouping = True)
				total = locale.format('%d', total_bytes[client_id], grouping = True)
				print("Received %s bytes from Client %d. Total: %s." % (bytes, client_id + 1, total))

