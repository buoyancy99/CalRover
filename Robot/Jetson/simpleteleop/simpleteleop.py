import serial
import socket


#TCP_IP = '2601:644:400:5b6b:bdce:61c5:afcc:6e48'
TCP_IP = '10.0.0.76'
BUFFER_SIZE = 20 
TCP_PORT = 5005
BUFFER_SIZE = 20

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
print('Connection to serial ' + ser.name + 'established.\n')

#s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT, 0, 0))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
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
