import cv2,time,pyautogui
from PIL import ImageGrab
import numpy as np
import pydirectinput as pyd
def go_forward():
    pyd.keyDown('w')
    time.sleep(0.1)
    pyd.keyUp('w')
    time.sleep(0.01)
def right():
    pyd.keyDown('d')
    time.sleep(0.0005)
    pyd.keyUp('d')
    time.sleep(0.0005)
def left():
    pyd.keyDown('a')
    time.sleep(0.0005)
    pyd.keyUp('a')
    time.sleep(0.0005)
ort_x = 0
ort_y = 0
ort_t = 0
duyarlilik = 10
lower_color = np.array([14,130,100])
upper_color = np.array([30,255,255])
time.sleep(2)
while 1:
    go_forward()
    ss = pyautogui.screenshot()
    ss = np.array(ss)
    ss = cv2.cvtColor(ss, cv2.COLOR_BGR2RGB)
    roi = ss[300:410,150:412]
    mask = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(mask,lower_color,upper_color)
    for x in range(mask.shape[1]): 
        for y in range(mask.shape[0]):
            if mask[y,x] == 255:
                ort_x+=x
                ort_y+=y
                ort_t+=1
    try:
        ort_x /= ort_t
        ort_y /= ort_t
        ort_x = int(ort_x)
        ort_y = int(ort_y)
        # cv2.circle(roi,(ort_x,ort_y),5,(255,0,0),-1)
        # cv2.circle(roi,(int(mask.shape[1]/2),int(mask.shape[0]/2)),5,(0,255,0),-1)
        cv2.imshow("ss",roi)
        if ort_x < int(mask.shape[1]/2) + duyarlilik and ort_x > int(mask.shape[1]/2) - duyarlilik:
            print("Yolunda")
        else:
            if ort_x < int(mask.shape[1]/2):
                left()
                print("left")
            if ort_x > int(mask.shape[1]/2):
                right()
                print("right")
    except:
        print("ALERT!!")
        go_forward()
    ort_t = 0
