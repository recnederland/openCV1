import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# blurring / detayi azaltir ve gurultuyu engeller
img= cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Orginal"),plt.show()

""" Ortalama Bulaniklastirma Yontemi """
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"),plt.title("Ortalama Blur")

""" Gaussian Blur """
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmax =7 )  
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gauss Blur")
# yukaridaki calismadi
gb2 = cv2.imread("NYC.jpg")
gaussian_blur = cv2.GaussianBlur(img, (5,5),0)
plt.figure(), plt.imshow(gaussian_blur), plt.axis("off"), plt.title("Gauss Blur")

""" Median Blur """
mb = cv2.medianBlur(img, ksize=(3,3), sigmax=7 ) # 
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Medyan Blur")
# yukaridaki calismadi
mb2 = cv2.imread("NYC.jpg")  
mblur = cv2.medianBlur(img, int(5),0)  
plt.figure(), plt.imshow(mblur), plt.axis("off"), plt.title("Medyan Blur")

                                                   
# resimler uzerine noise/  koyalim ki filtrelerin ise yaradigini inceleyebilelim
def gaussianNoise(image):
    row, col, ch = image.shape # ch=channel, resmin RGB 1 mi, grey mi
    mean = 0
    vary = 0.05
    sigma = vary**0.5 # sigma standart sapma 
    
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss 
    return noisy 

# normalizasyon ile 0-1 arasina sikkistiralim, bunun icin 255'e bolduk
img= cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Orginal"),plt.show()

# original foto uzerine gaussion noise ekleyelim ve gorelim
gaussianNoisyImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoisyImage), plt.title("Gauss Noisy"), plt.axis("off"),plt.show()

# gaussion blur ile olusturulan gurultu ve kirliligi azaltalim, goturelim
gb3 = cv2.GaussianBlur(gaussianNoisyImage, ksize=(3,3), sigmax=7 )  
plt.figure(), plt.imshow(gb3), plt.axis("off"), plt.title("with Gauss Blur"), plt.axis("off"),plt.show()


# simdi tuz/karabiber gurultusu ekleyelim ve daha sonra bunlari giderelim
def saltPapperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5 
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    # salt beyaz
    num_salt =np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    # papper siyah
    num_papper =np.ceil(amount * image.size * 1-s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_papper)) for i in image.shape]
    noisy[coords] = 0

    return noisy

# olusturdugumuz functionu noicy yapmak icin kullanalim
spImage = saltPapperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP Image")

# simdi fotodaki noisy'leri giderelim
mb4 = cv2.medianBlur(spImage.astype(np.float32), ksize= 3)
plt.figure(), plt.imshow(mb4), plt.axis("off"), plt.title("SP Image blur with median")










