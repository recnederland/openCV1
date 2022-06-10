import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("Orginal", img)

hori = np.hstack((img,img))
cv2.imshow("Horizontal", hori)

verti = np.vstack((img,img))
cv2.imshow("Vertical", verti)



k = cv2.waitKey(0) & 0xFF

if k == 27: # esc
    cv2. destroyAllWIndow()
elif k == ord('s'):
    cv2.imwrite("messi_grey.png", img)
    cv2.destroyAllWindows()