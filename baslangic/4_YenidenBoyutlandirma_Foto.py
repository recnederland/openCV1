import cv2

# fotoyu ice aktaralim
img = cv2.imread("lenna.png", 0)

# Foto boyutunu gorelim
print("Foto boyutu: ", img.shape)
 
# Fotoyu gorelim
cv2.imshow("Orjinal: ", img)

# Fotoyu yeniden boyutlandiralim
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape", imgResized.shape)
cv2.imshow("Img Resized", imgResized)

# Foto kirp
imgCropped = img[:200, :300] # OpenCV'de once yukseklik sonra genislik ve (-y, +x) ekseni
cv2.imshow("Kirpik foto", imgCropped)

 
k = cv2.waitKey(0) & 0xFF

if k == 27: # esc
    cv2. destroyAllWIndow()
elif k == ord('s'):
    cv2.imwrite("messi_grey.png", img)
    cv2.destroyAllWindows()






