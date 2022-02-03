#! /usr/bin/env python3
import http
from socket import *
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)

# True server address
origin_server_addr = ('127.0.0.1', 8889)	
# The proxy server is listening at 8888 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((sys.argv[1], 8888))
tcpSerSock.listen(100)

while 1:
	# Strat receiving data from the client
	print('Ready to serve...')
	## FILL IN HERE...
	clientSock, addr = tcpSerSock.accept()

	print('Received a connection from:', addr)

	message = clientSock.recv(1024).decode('utf-8')# FILL IN HERE...
	print(message)
	# Extract the filename from the given message
	sys.exit(-1)
	## FILL IN HERE...

	filetouse = None## FILL IN HERE...
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(origin_server_addr)
	try:
		# Check wether the file exist in the cache

		## FILL IN HERE...

		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n")            
		tcpCliSock.send("Content-Type:text/html\r\n")


		## FILL IN HERE...


	# Error handling for file not found in cache, need to talk to origin server and get the file
	except IOError:
		if fileExist == "false": 

			## FILL IN HERE...
			try:
				pass
			except:
				print("Illegal request")                                               
		else:
			# HTTP response message for file not found
			tcpCliSock.send("HTTP/1.0 404 sendErrorErrorError\r\n")                             
			tcpCliSock.send("Content-Type:text/html\r\n")
			tcpCliSock.send("\r\n")

	# Close the client and the server sockets    
	tcpCliSock.close() 
tcpSerSock.close()
