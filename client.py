import socket                
  
s = socket.socket()          
port = 9500                

# connect to localhost port 9500 
s.connect(('localhost', port)) 

#Send data to the server
req = s.send('Hello')

# receive data from the server 
res = s.recv(1024)
print(res)

# close the connection 
s.close()  