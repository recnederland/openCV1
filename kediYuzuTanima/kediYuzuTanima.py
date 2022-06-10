import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# fotolarin oldugu klasorun icerigini gorelim
files = os.listdir()
print(files)

# fotolari toplu ice aktarma
img_path_list = []
for f in files:
    print(f)
    if f.endswith(".jpg"):
        img_path_list.append(f)
print(img_path_list)

# simdi bu fotolari tek tek gezeleim
for i in img_path_list:
    print(i)
    image = cv2.imread(i)
# fotolari gezdirelim    
    cv2.imshow(i, image)
# q basildiginda kapatalim
    if cv2.waitKey(0) & 0xFF == ord('q'): continue

# Deneme 2

# yukarida fotolari sirayla gorduk simdi arayi doldurup yuzleri tespit edelim
# simdi bu fotolari tek tek gezeleim
for j in img_path_list:
    print(j)
    image = cv2.imread(j)
    
    # YUZ Tespit
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    rects = detector.detectMultiScale(gray, scaleFactor= 1.030, minNeighbors = 5) # scaleFactor resme zoom/scale orani
    # rects = detector.detectMultiScale(gray, scaleFactor= 1.045, minNeighbors = 2)
    # enumerate(rects) rectangle icindeki bilgileri ve indexi (i,(x,y,w,h))'a return eder
    for (i,(x,y,w,h)) in enumerate(rects): # tupl ((x,y,w,h))
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,255), 2 )
        # image, text, org, fontFace, fontScale, color
        cv2.putText(image, "Kedi {}".format(i+1), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,255,255), 2)
# fotolari gezdirelim    
    cv2.imshow(j, image)
# q basildiginda kapatalim
    if cv2.waitKey(0) & 0xFF == ord('q'): continue

