import socket

host = '0.0.0.0'
port = 8001

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
print(f'Listening on port {port} ...')

while True:
	client_connection, client_address = server_socket.accept()

	# Get the client request
	request = client_connection.recv(1024).decode()
	print(request)

	# Send HTTP response
	client_connection.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nDate: 9 Jan 2024\r\nHost: localhost:8001\r\n\r\n'.encode())
	client_connection.close()

server_socket.close()
print(f'Connection closed on port {port}.')
