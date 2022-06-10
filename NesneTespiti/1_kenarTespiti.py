import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi ice aktar
img = cv2.imread("london.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("original")

# kenarlari tespit etmeye calisalim
edges = cv2.Canny(image = img, threshold1 = 0, threshold2 = 255)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off"), plt.title("Kenar 1")

med_val = np.median(img)
print(med_val)

low = int(max(0, (1 - 0.33) * med_val))
high = int(max(255, (1 + 0.33) * med_val))
print(low)
print(high)

edges2 = cv2.Canny(image = img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges2, cmap = "gray"), plt.axis("off"), plt.title("Kenar 2")

# blur
blurred_img = cv2.blur(img, ksize=(5,5))
plt.figure(), plt.imshow(blurred_img, cmap = "gray"), plt.axis("off")

# tekrar 
med_val = np.median(img)
print(med_val)

low = int(max(0, (1 - 0.33) * med_val))
high = int(max(255, (1 + 0.33) * med_val))
print(low)
print(high)

edges3 = cv2.Canny(image = blurred_img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges3, cmap = "gray"), plt.axis("off"), plt.title("Kenar 3")


