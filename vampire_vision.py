import numpy as np
import cv2
import matplotlib.pyplot as plt

#initialise
seconds = np.arange(0,61)
brightness = np.ones(61)
fig,ax = plt.subplots()
line, = ax.plot(seconds, brightness)

#get video
cap = cv2.VideoCapture(0)
cap.set(3,640)  #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(4,480)  #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(5, 30) #cap.set(cv2.CAP_PROP_FPS, 30)
# cap.set(10,1000) #set brightness


while True:
    success, img = cap.read()
    cv2.imshow('Video',img)
    current_brightness = 8
    brightness[0], brightness[1:] = current_brightness, brightness[0:-1]
    line.set_ydata(brightness)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break