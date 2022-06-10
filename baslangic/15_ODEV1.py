# openCV kutuphanesini ice aktaralim
import cv2

# matplotlib.plotly ve numpy kutuphanesini ice aktaralim
import numpy as np
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak cizdirelim
img = cv2.imread("odev1.jpg", 0)
cv2.imshow("Odev-1", img)
# resmin boyutuna bakalim
img_shape = img.shape
print(img_shape) # (568, 860, 3)

# resmi 4/5 boyutunda yeniden cizdirelim ve resmi cizdirelim
# img_reshape = cv2.resize(img,(450,650))
# plt.figure(), plt.imshow(img_reshape), plt.axis("off"), plt.title("Odev Reshape 4/5")
img_reshape = cv2.resize(img,(int(img.shape[1]*4/5), int(img.shape[0]*4/5)))
cv2.imshow("Yeniden Boyutlandirilmis 4/5", img_reshape)

# resme bir yazi ekletelim ve resmi cizdirelim "kopek"
# img_text = cv2.putText(img, "IMG with text", (300,300), cv2.FONT_HERSHEY_COMPLEX, 1, (250,250,250))
# plt.figure(), plt.imshow(img_text), plt.axis("off"), plt.title("Odev Text")
img_text = cv2.putText(img, "Kopek", (375,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
cv2.imshow("Kopek", img_text)
# orinal resmi 50 threshold degeri uzerindekileri beyaz altindakileri ise siyah yapalim
_, thresh_img = cv2.threshold(img, thresh=50, maxval=255, type=cv2.THRESH_BINARY)
# plt.figure(), plt.imshow(thresh_img), plt.axis("off"), plt.title("Odev Treshhold")
cv2.imshow("Treshold", thresh_img)
# daha sonra adaptiveThreshold ve  binary yontemi kullanalim ve resmi cizdirelim
thresh_binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
cv2.imshow("Treshold binary", thresh_binary)

# orginal resme gaussian bulaniklastirma uygulayalim ve resmi cizdirelim
guassian_img = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
cv2.imshow("Gaussian Blur ile berraklik", guassian_img)

# orjinal resme Laplacian gradyan uygulayalim ve resmi cizdirelim
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F)
cv2.imshow("Laplacian", laplacian)

# orjinal resmin histogramini cizdirelim
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)














