import cv2
import matplotlib.pyplot as plt
import numpy as np

# foto ice aktarma
img = cv2.imread("datai_team.jpg")
plt.figure(), plt.imshow(img, cmap= "gray"), plt.axis("off"), plt.title("original datai team"), plt.show()

# erezyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 2)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")

# genisletme / dailation, erozyonun tersi
result2 = cv2.dilate(img, kernel, iterations = 2)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genisleme")

# acilma icin once white noise / beyaz gurultu yapalim


# daraltma



# kapama


# morfolojik

