import serial
import socket
import requests
from semail import send_simple_message

ipdoc = open("ip.txt","r")
previp = ipdoc.readline()
curip = requests.get('http://ident.me').text
ipdoc.close()
print(previp, curip)

if previp != curip :
    ipdoc = open("ip.txt","w")
    ipdoc.write(curip)
    send_simple_message(curip)
    ipdoc.close()
    

TCP_IP = 'localhost'

BUFFER_SIZE = 20 
TCP_PORT = 5005
BUFFER_SIZE = 20

if len(TCP_IP) > 15:
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT, 0, 0))
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
print('Connection to serial ' + ser.name + 'established.\n')


s.listen(1)

conn, addr = s.accept()
print ('TCP Connection address: ', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    d = data.decode("ascii")
    try:
        print ("received data: ", d[0], ord(d[1]), ord(d[2]))
    except:
        pass
    conn.send(data)  # echo
    ser.write(data)
    d = ser.read()
    print(d)
conn.close()
ser.close()          

