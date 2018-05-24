import socket
import cv2
import numpy as np
import sys

def nothing(x):
    pass

TCP_IP = '107.77.75.66'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('L','image',  64, 127 ,nothing)
cv2.createTrackbar('R','image', 64 , 127 ,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    l = cv2.getTrackbarPos('L','image')
    r = cv2.getTrackbarPos('R','image')

    if l < 0:
        l = 64
    if r < 0:
        r = 64

    print (l, r)
    switchvalue = cv2.getTrackbarPos(switch,'image')
    if switchvalue == 0:
        l = r = 64

    message = ("#" + chr(l) + chr(r)).encode(("ascii"))
    s.send(message)
    #s.send(chr(l).encode("utf-8"))
    #s.send(chr(r).encode("utf-8"))
    #s.send(l.to_bytes(1, byteorder=sys.byteorder))
    #s.send(r.to_bytes(1, byteorder=sys.byteorder))


cv2.destroyAllWindows()
s.close()