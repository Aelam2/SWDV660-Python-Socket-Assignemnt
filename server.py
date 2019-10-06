import socket
import logging
import logstash
import sys

host = '54.237.168.58'

test_logger = logging.getLogger('python-application-log')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))

s = socket.socket()
port = 9500
s.bind(('', port)) 
test_logger.info("Socket bound to port {}".format(port))

s.listen(5)
test_logger.info("Socket is listening")

while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()

    message = ''
    if(data.lower() == 'hello'):
        message = 'Hi'
        test_logger.info('Connected IP Address: {}. Request Data: {}. Response Data: {}'.format(addr, data, message))

    else:
        message = 'Goodbye'
        test_logger.warning('Connected IP Address: {}. Request Data: {}. Response Data: {}'.format(addr, data, message))



    conn.send(message.encode())
    conn.close()