from socket import *
host = '127.0.0.1'
port = 9999

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

msg = "client"
s.send(msg.encode("ascii"))
R_msg = s.recv(1024)
print(R_msg.decode('ascii'))

s.close()
