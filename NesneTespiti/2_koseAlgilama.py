import cv2
import matplotlib.pyplot as plt
import numpy as np

# fotoyu gorelim
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Sudoku original")

# harris corner detection
dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off"), plt.title("Corner Harris")

dst2 = cv2.dilate(dst, None)
img[dst2>0.2 * dst.max()] = 1
plt.figure(), plt.imshow(dst2, cmap = "gray"), plt.axis("off"), plt.title("Corner Harris II")

# shi tomasi detection
img2 = cv2.imread("sudoku.jpg", 0)
img2 = np.float32(img2)
corners = cv2.goodFeaturesToTrack(img2, 100, 0.01, 10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img2, (x,y), 3, (125,125,125), cv2.FILLED)
    
plt.imshow(img2), plt.axis("off"), plt.title("Shi Tomasi Detection")





