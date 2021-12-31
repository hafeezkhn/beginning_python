from socket import *
host = '127.0.0.1'
port = 9999

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("[+]got connection", addr)
    R_msg = c.recv(1024)
    print(R_msg.decode('ascii'))
    msg = "Server"
    c.send(msg.encode('ascii'))
    c.close()
