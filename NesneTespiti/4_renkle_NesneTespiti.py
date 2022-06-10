import cv2
import matplotlib.pyplot as plt
import numpy as np
from collections import deque # tespit ettigimiz nesnenin merkezini belirlemek icin

# buffer_size ile nesne merkezini depolayacak veri type
buffer_size = 16
pts = deque(maxlen = buffer_size)

# nesne tespiti icin mavi renk araligi kullanalim
# HSV sklasinda H = ton, S = doygunluk, V = parlaklik
blueLower = (84, 98, 0)
blueUpper = (179, 255, 255)

# capture
cap = cv2.VideoCapture(0)
cap.set(3,960) # genislik 
cap.set(3,960) # ve yukseklik kamerada

while True:
    
    success, imOriginal = cap.read()
    
    if success:
        # blur ile noise azaltalim
        blurred = cv2.GaussianBlur(imOriginal, (11,11), 0)
        # hsv
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)
        cv2.imshow("HSV Image", hsv)
        #mavi icin maske olusturalim
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("Mask Image", mask)
        # maskenin etrafinda kalan gurultuleri erozyon ve genisleme ile sil
        mask = cv2.erode(mask, None, iterations = 2)
        mask = cv2.dilate(mask, None, iterations = 2)
        cv2.imshow("Mask + Erozyon ve Genisletme ", mask)
        
        # contourleri bulalim
        (contours,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        center = None
        
        if len(contours) > 0:
            # en buyuk kontutu alalim
            c= max(contours, key = cv2.contourArea)
            # dikdortgene cevir, rectengle
            rect = cv2.minAreaRect(c)
            ((x,y), (width, height), rotation) = rect 
            s = "x: {}, width: {}, height: {}, rotation: {}".format(np.round(x), np.round(y), np.round(height), np.round(rotation))
            print(s)
         
            # nesnenin etrafini kaplamak icin kutucuk hazirlayalim
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            
            # moment ile goruntunun merkezini bulabiliriz
            M = cv2.moments(c)
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            
            # konturu cizdirelim: sari,   drawContours(image, contours, contourIdx, color)
            cv2.drawContours(imOriginal, [box], 0, (0,255,255), 2)
             
            # merkeze bir nokta cizelim
            cv2.circle(imOriginal, center, 5, (255,0,255), -1)
            
            # bilgileri ekrana yazdiralim, putText(img, text, org, fontFace, fontScale, color)
            cv2.putText(imOriginal, s, (25,25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 2)
            
        # deque ile ufak bir takip calismasi yapalim
        pts.appendleft(center)
        
        for i in range(1, len(pts)):
            if pts[i-1] is None or pts[i] is None: continue
            cv2.line(imOriginal, pts[i-1], pts[i], (0,255,0), 3)
        
        cv2.imshow("Original Tespit", imOriginal)
        
    if cv2.waitKey(1) & 0xFF == ord("q"): break       
        
        
        
        
        






