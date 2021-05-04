import socket
import sys

# TCP Sockets

try:
	sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
except socket.error as err:
	print('Failed o create a Socket')
	print(f'Error {str(err)}')
	sys.exit()
else:
	print('Socket created successfully')


target_host = input('Enter the target Hostname to connect: ')
target_port = int(input('Enter the target PORT number: '))

try:
	sock.connect((target_host, target_port))
	print('Connection Established successfully')
	sock.shutdown(2)
except socket.error as err:
	print(f'Failed to connect due to : {str(err)}')
	sock.shutdown(2)
else:
	print(f'Socket connected to {target_host} @ {target_port}')
