# !pip install opencv-python
import cv2



# Resmi Ice Aktarma
img = cv2.imread("messi1.png", 0)

# gorsellestir
cv2.imshow("Ilk resim", img)

# Fotograflar iki boyutlu matrsilerdir

k = cv2.waitKey(0) & 0xFF

if k == 27: # esc
    cv2. destroyAllWIndow()
elif k == ord('s'):
    cv2.imwrite("messi_grey.png", img)
    cv2.destroyAllWindows()






