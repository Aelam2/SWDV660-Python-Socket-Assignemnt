import socket

s = socket.socket()
port = 9500
s.bind(('', port)) 
print("Socket bound to port", port)

s.listen(5)
print("Socket is listening")

while True:
    conn, addr = s.accept()
    print("Connection from", addr)

    data = conn.recv(1024).decode()
    print('Client data:', data)
    
    message = ''
    if(data.lower() == 'hello'):
        message = 'Hi'
    else:
        message = 'Goodbye'

    conn.send(message.encode())
    conn.close()