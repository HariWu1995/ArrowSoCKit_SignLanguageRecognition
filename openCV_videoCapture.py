# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:36:21 2017

@author: Hari Wu
"""

import numpy as np
import cv2

capture = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 20.0
frameSize = (640,480)
output = cv2.VideoWriter('webcam.avi',fourcc,fps,frameSize)

while(True):
    ret, frame = capture.read()     # Capture frame-by-frame
    if ret == True:
        # frame = cv2.flip(frame,0)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        output.write(gray)         # write the flipped frame
        cv2.imshow('frame',gray)   # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
capture.release()                   # Release the capture
output.release()
key = cv2.waitKey(0)                # 64-bit: key = cv2.waitKey(0) & 0xFF
if key == 27:                       # ESC key
    cv2.destroyAllWindows()