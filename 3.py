import socket

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

payload = "Hey Server, How's it going????"

try:
	while True:
		client_socket.send(payload.encode('utf-8'))
		data = client_socket.recv(1024)
		print(str(data))
		more_input = input('Do you wanna send more data: ')

		if more_input.lower() == 'y':
			payload = input('Enter your message: ')
		else:
			print('Thanks for communication')
			break
except KeyboardInterrupt:
	print('Exited by the user')

client_socket.close()
