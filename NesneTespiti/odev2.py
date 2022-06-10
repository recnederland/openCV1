# opencv numpy kutuphanelerini iceri aktaralim
import cv2
import numpy as np
# resmi siyah beyaz olarak ice aktaralim
img = cv2.imread("odev2.jpg", 0)

# resmi cizdirelim ve kenarlari belirleyelim gorsellestirelim
cv2.imshow("Odev2", img)

# resmi uzerinde bulunan kenarlari tespit edelim ve gorsellestirelim, edge detection
edges = cv2.Canny(image = img, threshold1 = 200, threshold2 = 255)
cv2.imshow("Kenar Tespiti", edges)

# yuz tespiti icin gerekli haar cascade iceri aktar
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# yuz tespiti yapip sonuclari gorsellestirelim
face_rect = face_cascade.detectMultiScale(img)

for (x,y,w,h) in face_rect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 10)
cv2.imshow("Yuz Tespiti", img)

# initialize the HOG (ilklendirelim) insan tespiti algoritmasini cagiralim ve SVN'i set edelim
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector)

# Resme insan tespiti algoritmamizi uygulayalim ve gorsellestirelim
(rects, weights) = hog.detectMultiScale(img, padding = (8,8), scale = 1.05)

for (xA, yA, xB, yB) in rects:
    cv2.rectangle(img, (xA,yA), (xB,yB), (0,0,255), 2)

cv2.imshow("Insan Tespiti", img)











