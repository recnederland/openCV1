import cv2
import matplotlib.pyplot as plt

# fotoyu gorelim

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grey, siyah beyaza yakin, grey skala
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.show()


# fotoyu siyah beyaz hale getirelim genlik degerleri 255'e yakinsa beyaz, 0'a yakinsa siayaha yaklasir

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grey, siyah beyaza yakin, grey skala
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

# fotoya esik belirleyerek esik ustunu yok edelim threshold =esik

_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY) # THRESH_BINARY_INV
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

# threshold kullandigimizda nesnelerin butunlugu bozulmasin diye adaptiveThreshold kullanacagiz
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()
