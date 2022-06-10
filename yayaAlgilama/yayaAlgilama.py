import cv2
import os

# file okuyalim
files = os.listdir()
img_path_list = []

for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
        
print(img_path_list)

# hog tanimlayicisi
hog = cv2.HOGDescriptor()
# tanimlayiciya SVM ekle
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for imagePath in img_path_list:
    print(imagePath)
    
    image = cv2.imread(imagePath)
    # tuple donecek asagidaki
    (rects, weight) = hog.detectMultiScale(image, padding = (7,7), scale = 1.01)
    # (rects, weight) = hog.detectMultiScale(image, padding = (8,8), scale = 1.05)
    for (x,y,w,h) in rects:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)
        
    cv2.imshow("Yaya:", image)
    
    if cv2.waitKey(0) & 0xFF == ord("q"): continue









