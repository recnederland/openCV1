import cv2
import numpy as np
import matplotlib.pyplot as plt

# fotoyi gorelim
einstein = cv2.imread("einstein.jpg",0)
plt.figure(), plt.imshow(einstein), plt.axis("off")

# simdi yuzu gorelim siniflandirici / clasificare
# bunu siniflandirici pozitif ve negatif veriler uzerinden egitilir yuzu tanimaz henuz var mi/ yok mu

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(einstein)
# pixcel pixcel tarayarak yuzu bulur kucukten buyuge kareleri genisleterek
for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y), (x+w, y+h), (255,255,255), 10)
    
plt.figure(), plt.imshow(einstein, cmap = "gray"), plt.axis("off"), plt.title("Einstein1")

# simdi kalabalik bir grup icinde bu islemi yapalim
barce = cv2.imread("barcelona.jpg", 0)
plt.figure(), plt.imshow(barce, cmap = "gray"), plt.axis("off"), plt.title("barce 1")

face_rect = face_cascade.detectMultiScale(barce, minNeighbors = 10)

for (x,y,w,h) in face_rect:
    cv2.rectangle(barce, (x,y), (x+w, y+h), (255,255,255), 10)
    
plt.figure(), plt.imshow(barce, cmap="gray"), plt.axis("off"), plt.title("Barcelona Team")

# videoda yuz saptama
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    if ret:
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
        
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 10)
        cv2.imshow("face detect", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

























