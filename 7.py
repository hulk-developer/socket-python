import socket

host = '127.0.0.1'
port = 1233


client_socket = socket.socket()

print('Waiting for connection')

try:
	client_socket.connect((host, port))
except socket.error as e:
	print(f'Error: {e}')


res = client_socket.recv(1024)
print(res.decode('utf-8'))

while True:
	data = input('Enter your message: ')
	client_socket.send(data.encode('utf-8'))
	response = client_socket.recv(1024)
	print(response.decode('utf-8'))
