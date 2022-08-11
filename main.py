import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

#window params
height,width = 1080,1900

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)


detector = HandDetector(maxHands=1, detectionCon=0.8)

#Comms
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddr = ("127.0.0.1", 5052)

while(True):
    #img cap
    success, img = cap.read()

#get hand data from previous cap
    hands,img = detector.findHands(img)

    #get values of the hand data
    data = []
    if hands:
        hand = hands[0]
        lmlist = hand['lmList']
        #lmList data
        for lm in lmlist:
            data.extend([lm[0],height-lm[1],lm[2]])
        print(data)
        sock.sendto(str.encode(str(data)),serverAddr)
    cv2.imshow("img",img)
    cv2.waitKey(1)
