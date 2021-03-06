import cv2
import matplotlib.pyplot as plt

# ana foto ile tespit edecegimiz nesneyi gorelim
chos = cv2.imread("chocolates.jpg", 0)
plt.figure(), plt.imshow(chos, cmap ="gray"), plt.axis("off")

cho = cv2.imread("nestle.jpg", 0)
plt.figure(), plt.imshow(cho, cmap ="gray"), plt.axis("off")

# orb tanimlayici, kose-kenar gibi nesneye ait ozellikler, anahtar noktalar
orb = cv2.ORB_create()

# anahtar nokta tespiti, description
kp1, des1 = orb.detectAndCompute(cho, None) # maskeleme yok None
kp2, des2 = orb.detectAndCompute(chos, None)

# bf matcher, bloetforce
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# noktalari eslestirme
matches = bf.match(des1, des2)

# mesafeye gore siralayalim ve istedigimiz araligi gorsellestirelim
matches = sorted(matches, key = lambda x: x.distance)

# eslesen resimleri gorsellestirme
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags =2)
plt.imshow(img_match), plt.axis("off"), plt.title("Orb")

# yoksa yukleyelim: pip install opencv-contrib-python --user
# sift tanimlayicisini kullanalaim bu sefer orb yerine
sift = cv2.xfeatures2d.SIFT_create()

# bloetforce matcher
bf = cv2.BFMatcher()

# anahtar nokta tespiti, sift ile
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(cho, None)

matches = bf.knnMatch(des1, des2, k = 2)

guzel_eslesme = []

for match1, match2 in matches:
    
    if match1.distance < 0.75 * match2.distance:
        guzel_eslesme.append([match1])
        
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, guzel_eslesme, None, flags = 2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("Sift")













