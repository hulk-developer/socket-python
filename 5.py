import socket

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

msg = 'I love VueJS and React too'
client_socket.sendto(msg.encode('utf-8'), ('127.0.0.1', 12345))

data, addr = client_socket.recvfrom(4096)

print(f'From Server: {str(data)}')
client_socket.close()
