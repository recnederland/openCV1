# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:51:42 2022

@author: recba
"""

import cv2
import time

# video ismi
video_name = "MOT17-04-DPM.mp4"

# video ice aktar: capture, cap
cap = cv2.VideoCapture(video_name)

print("Genislik: ", cap.get(3))
print("Yukseklik: ", cap.get(4))

if cap.isOpened() == False:
    print("Hata")
    
while True:
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.01) # uyari: deger kullanmazsak cok hizli akar
        
        cv2.imshow("Video", frame)
    else: break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # stop capture
cv2.destroyAllWindows()