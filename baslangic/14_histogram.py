import cv2
import matplotlib.pyplot as plt
import numpy as np

# kirmizi/mavi foto
img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis)

print(img.shape) # (371, 366, 3)

# histogrami cizdirelim
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist)
plt.figure(), plt.plot(img_hist)

# histogrami renkleri ayirarak r,g,b, daha iyi gorelim
color = ("b", "g", "r")
plt.figure()
for i, c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color=c)

# 2. foto goldenGate gorelim
golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate_vis)

print(golden_gate.shape) # (2448, 3264, 3)

# resmin kirmizilari maskeyle gormeye calisicaz, once maske yapalim
mask = np.zeros(golden_gate.shape[:2], np.uint8) # interger yapmak icin__np.uint8
plt.figure(), plt.imshow(mask, cmap = "gray")

# maskeyi filtreleyelim ve bir kismini alalim
mask[1500:2000, 1000:2000] = 255
plt.figure(), plt.imshow(mask, cmap = "gray")

# simdi hazirladigimiz maskenin icinde actigimiz bolgeyi resmimiz uzerinde gorelim
mask_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask= mask)
plt.figure(), plt.imshow(mask_img_vis, cmap = "gray")

# histogramimizi uygulayalim kirmizi icin
masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask= mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [0], mask = mask, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(masked_img_hist) 

# histogramimizi uygulayalim mavi icin
masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask= mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [2], mask = mask, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(masked_img_hist) 

# histogramimizi uygulayalim kirmizi icin
masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask= mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [1], mask = mask, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(masked_img_hist) 

# histogram esitleme ve konstrat/karsitlik artirma
img2 = cv2.imread("hist_equ.jpg")
plt.figure(), plt.imshow(img2, cmap = "gray")
# 3. resmi kullanarak renklerin konstratlari artirilacak
img2 = cv2.imread("hist_equ.jpg", 0)
plt.figure(), plt.imshow(img2, cmap = "gray")
# histogrami cizdirelim
img_hist = cv2.calcHist([img2], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)
# equalise/esitleme islemi yapalim
eq_hist = cv2.equalizeHist(img2)
plt.figure(), plt.imshow(eq_hist, cmap = "gray")
# equalizenin histogrami cizdirelim
eq_img_hist = cv2.calcHist([eq_hist], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(eq_img_hist)

