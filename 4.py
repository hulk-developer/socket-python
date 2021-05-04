# UDP sockets
import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 12345))

while True:
	data, addr = sock.recvfrom(4096)

	print(f'Data received from cient: {data}')
	message = 'This is a UDP server...'

	sock.sendto(message.encode('utf-8'), addr)
