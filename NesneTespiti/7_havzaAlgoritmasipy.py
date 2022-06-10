import  cv2
import matplotlib.pyplot as plt
import numpy as np

# fotoyu ice aktaralim
coin = cv2.imread("coins.jpg")
plt.imshow(coin)

# fotodaki madeni paralarin etrafindaki girintileri bluring islemiyle kaldiralim
coin_blur = cv2.medianBlur(coin, 13)
plt.figure(), plt.imshow(coin_blur), plt.axis("off"), plt.title("Blur Coin 1")

# grayScale uygulayarak fotoyu siyah beyaz yapalim
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray), plt.axis("off"), plt.title("GrayScale 1")

# binary threshold
ret, coin_thresh = cv2.threshold(coin_gray, 75, 255, cv2.THRESH_BINARY)
plt.figure(), plt.imshow(coin_thresh, cmap="gray"), plt.axis("off"), plt.title("Threshold Gray")

# kontur uygulayalim ve paralari ayirmaya calisalim
contours, hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin, contours, i, (0,255, 0), 10)
plt.figure(), plt.imshow(coin), plt.axis("off")

# Sonuc istedigimiz gibi olmadi baska bir yontemle son kismi yapalim
# SEGMENTATION 

# fotoyu ice aktaralim
coin = cv2.imread("coins.jpg")
plt.imshow(coin)

# fotodaki madeni paralarin etrafindaki girintileri bluring islemiyle kaldiralim
coin_blur = cv2.medianBlur(coin, 13)
plt.figure(), plt.imshow(coin_blur), plt.axis("off"), plt.title("Blur Coin 1")

# grayScale uygulayarak fotoyu siyah beyaz yapalim
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray), plt.axis("off"), plt.title("GrayScale 1")

# binary threshold
ret, coin_thresh = cv2.threshold(coin_gray, 65, 255, cv2.THRESH_BINARY)
plt.figure(), plt.imshow(coin_thresh, cmap="gray"), plt.axis("off"), plt.title("Threshold Gray")

# count arasindaki sinirlari belirginlestirmek icin once erezyon sonra acilma yontemini kullanalim
# acilma
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(coin_thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off")

# nesneler arasinda distance bulalim
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
plt.figure(), plt.imshow(dist_transform, cmap = "gray"), plt.axis("off")

# ondeki nesneleri bulmak icin onlari kucultelim
# ret = return
ret, sure_foreground = cv2.threshold(dist_transform, 0.4 * np.max(dist_transform), 255, 0)
plt.figure(), plt.imshow(sure_foreground, cmap="gray"), plt.axis("off")

# arkaplani bumak icin cisimleri buyutelim
sure_background = cv2.dilate(opening, kernel, iterations = 1)
sure_foreground = np.uint8(sure_foreground)
unknown = cv2.subtract(sure_background, sure_foreground)
plt.figure(), plt.imshow(unknown, cmap = "gray"), plt.axis("off")

# baglanti
ret, marker = cv2.connectedComponents(sure_foreground)
marker = marker + 1
marker[unknown == 255] = 0
plt.figure(), plt.imshow(marker, cmap = "gray"), plt.axis("off")

# havza algoritmasi ile resimlri tekrar tespit edelim
marker = cv2.watershed(coin, marker)
plt.figure(), plt.imshow(marker, cmap = "gray"), plt.axis("off")

# kontur uygulayalim ve paralari ayirmaya calisalim kirmiziyla
contours, hierarchy = cv2.findContours(marker.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin, contours, i, (255,0, 0), 10)
plt.figure(), plt.imshow(coin), plt.axis("off")





