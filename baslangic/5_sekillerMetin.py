import cv2
import numpy as np

# foto olustur
img = np.zeros((512,512,3), np.uint8) # siyah bir resim (piksel 0'a yakin demektir)
print(img.shape)
cv2.imshow("Siyah", img)

# cizgi
# once foto, sonra baslangic noktasi, bitis noktasi, renk, kalinlik
cv2.line(img, (0,0), (512,512), (0,255,0),3) # BGR = (0,255,0)
cv2.imshow("Cizgi", img)

cv2.line(img, (100,100), (100,300), (0,255,0),3) # BGR = (0,255,0)
cv2.imshow("Cizgi2", img)

# dikdortgen
cv2.rectangle(img, (0,0), (256,256), (255,0,0),cv2.FILLED) # BGR = (0,255,0)
cv2.imshow("Dikdortgen", img)

# cember
cv2.circle(img, (0,0), (0,0), 45, (0,0,256),cv2.FILLED) # BGR = (0,255,0)
cv2.imshow("Cember", img)

# daire
# cv2.circle(img, (0,0), (int(300), int(300)), 45, (0,0,255), cv2.FILLED) # BGR = (0,255,0)
# cv2.imshow("Dairen", img)

# metin
# foto, baslangic koordinati, font, kalinligi, renk
cv2.putText(img, "Foto", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)

k = cv2.waitKey(0) & 0xFF

if k == 27: # esc
    cv2. destroyAllWIndow()
elif k == ord('s'):
    cv2.imwrite("messi_grey.png", img)
    cv2.destroyAllWindows()





