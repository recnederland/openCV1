import cv2
import numpy as np

img = cv2.imread("kart.png")
cv2.imshow("kart", img)

width = 400
height = 500

pts1 = np.int32([[230,1][1,472],[540,150],[338,617]])
pts2 = np.int32([[0,0],[0,height], [width,0], [width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

# son foto hali 
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Foto Son Hali", imgOutput)

# val = val + img[x+j][y+i]*matrix[row][col] 


k = cv2.waitKey(0) & 0xFF

if k == 27: # esc
    cv2. destroyAllWIndow()
elif k == ord('s'):
    cv2.imwrite("messi_grey.png", img)
    cv2.destroyAllWindows()