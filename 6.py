# Multi-threaded server
from threading import _start_new_thread
import socket

host = '127.0.0.1'
port = 1233
thread_count = 0

server_socket = socket.socket()

try:
	server_socket.bind((host, port))
except socket.error as e:
	print(str(e))

print('Waiting for connection')

server_socket.listen(5)


def client_thread(connection):
	msg = 'I am your Server'
	encoded_msg = msg.encode('utf-8')
	connection.send(encoded_msg)

	while True:
		data = connection.recv(2048)
		reply = 'I heard you ' + data.decode('utf-8')
		encoded_reply = reply.encode('utf-8')
		if not data:
			break
		connection.send(encoded_reply)
	connection.close()


while True:
	client, addr = server_socket.accept()
	print(f'Connected to {addr[0]} @ {addr[1]}')
	thread_count += 1
	print(f'Thread Count = {thread_count}')
	_start_new_thread(client_thread, (client,))

server_socket.close()
