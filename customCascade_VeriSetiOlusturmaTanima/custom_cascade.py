import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


"""
    NE YAPACAGIZ?
    1- veri seti (p/pozitif ve n/negatif fotolar olacak icinde)
    2- cascade programi indir
    3- cascade yap
    4- cascade kullanarak tespit algoritmasi yap

"""
# Foto depo klasoru
path = "images"

# resim boyutu
imgWidth = 180
imgHeight = 120

# video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640) # genislik
cap.set(4, 480) # boyut
cap.set(10, 180) # brighnist / aydinlik ayari

# klasor olusturma

global countFolder
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(path + str(countFolder)):
        countFolder +=1
    os.makedirs(path + str(countFolder))
    
saveDataFunc()

# 2- Veri setini positif ve negatif olarak olusturalim
# simdi kamerayi acarak seri halinde fotolari cekmek icin kodumuzu yazalim
# once bir klasore inceleyecegimiz cisimlerin forosuu alip p yapalim. negatifleri ikinci bir klsaore koyalim
count = 0
countSave = 0

while True:
    
    success, img = cap.read()
    
    if success: # birseyler okuyabiliyorsak
        # kamera buyuk boyutlu acilacak simdi resimleri olceklendirip kucultelim
        img = cv2.resize(img, (imgWidth, imgHeight))
        # hizli veri toplancak cok sayida. hepsini almak istemeyiz, sinir koyalim
        if count % 5 == 0:
            cv2.imwrite(path+str(countFolder)+"/" + str(countSave) + "_" + ".png", img)
            countSave += 1
            print(countSave)
        count += 1
        
        cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break 
    
cap.release()
cv2.destroyAllWindows()

# 3- cascade olusturalim
# simdi cascade programini indirelim. bu sitede kullanim aciklamasi da var
# https://amin-ahmadi.com/cascade-trainer-gui/ 
# islemi turkce kakter path olmayan bir yerde ornegin D'de yapip cascade.xml dosyasini classifier'dan 
# alip kendi dosyamiza tasiyabiliriz
# simdi bir sayfa .py acalim oradan devam edelim







