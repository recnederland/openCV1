import cv2




# 3- cascade olusturalim
# simdi cascade programini indirelim. bu sitede kullanim aciklamasi da var
# https://amin-ahmadi.com/cascade-trainer-gui/ 
# islemi turkce kakter path olmayan bir yerde ornegin D'de yapip cascade.xml dosyasini classifier'dan 
# alip kendi dosyamiza tasiyabiliriz
# simdi bir sayfa .py acalim oradan devam edelim

# path = "cascade.xml" , asagida kullanildigi icin comment altina aldik
objectName = "Kalem Ucu"

frameWidth = 280 
frameHeight = 360  
color =  (255,0,0)

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# empty olarak createTrackbar icinde cagiracagimiz functionu pass olarak verelim
def empty(a): pass

# trackbar / scale degisikligi icin
cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc", frameWidth, frameHeight + 100)
cv2.createTrackbar("Scale", "Sonuc", 400, 1000,empty ) # trackbarName, windowName, value, count, onChange
cv2.createTrackbar("Neighbor", "Sonuc", 4,50,empty) # empty

# cascade classifier
cascade = cv2.CascadeClassifier("cascade.xml")

while True:
    # read img
    success, img = cap.read()
    # convert BGR2GRAY
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # parameters of detection
        scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Sonuc") / 1000) # (trackbarname, winname)
        neighbor = cv2.getTrackbarPos("Neighbor", "Sonuc")
        # detection with rectangles
        rects = cascade.detectMultiScale(gray, scaleVal, neighbor)
        
        for (x,y,w,h) in rects:
            
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 3)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2) # img, text, org, fontFace, fontScale, color
        cv2.imshow("Sonuc", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

    
    
    
    
    
