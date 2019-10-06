import socket    
import random 
  
s = socket.socket()          
port = 9500                

# connect to localhost port 9500 
s.connect(('localhost', port)) 

#The none value is for invoking an error to log to the server
possibleRequestMessages = ['Hello', 'Test', 'Bye']

#Send data to the server
req = s.send(random.choice(possibleRequestMessages))

# receive data from the server 
res = s.recv(1024)
print(res)

# close the connection 
s.close()  