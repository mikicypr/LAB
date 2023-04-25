import cv2
import numpy as np

sciezka=r"C:\Users\Johny017\Desktop\zdj\original.jpg"
sciezka_zapis=r"C:\Users\Johny017\Desktop\zdj\bayer.jpg"
zapis_identity=r"C:\Users\Johny017\Desktop\zdj\identity.jpg"
zapis_kernel=r"C:\Users\Johny017\Desktop\zdj\blur_kernel.jpg"

im=cv2.imread(sciezka)
#im = cv2.resize(im,None,fx=1/3,fy=1/3,interpolation=cv2.INTER_NEAREST)
cv2.imshow('original',im)

height, width = im.shape[:2]
print(height,width)
B,G,R=cv2.split(im)

#print(B,G,R)

bayer_filter=np.empty((height,width), np.uint8)
fuji_filter=np.empty((height,width), np.uint8)

#GR
#BG

bayer_filter[0::2, 0::2]=G[0::2, 0::2] #lewy gorny zielony
bayer_filter[0::2, 1::2]=R[0::2, 1::2] #prawy gorny czerwony
bayer_filter[1::2, 0::2]=B[1::2, 0::2] #lewy dolny niebieski
bayer_filter[1::2, 1::2]=G[1::2, 1::2] #prawy dolny zielony

print(bayer_filter[:10, :10])
cv2.imshow('szary', bayer_filter)

bayer_filter=cv2.cvtColor(bayer_filter, cv2.COLOR_GRAY2BGR)

bayer_filter[0::2, 0::2, 0::2] = 0  #zielony piksel, zamiana czerownego i niebieskiego na 0
bayer_filter[0::2, 1::2, 0:2] = 0   # czerwony piksel, zamiana zielonego i niebieskiego na 0
bayer_filter[1::2, 0::2, 1:] = 0    # niebieski piksel, zamiana zielonego i czerwonego na 0
bayer_filter[1::2, 1::2, 0::2] = 0  #zielony piksel, zamiana czerownego i niebieskiego na 0

#bayer_filter = cv2.resize(bayer_filter,None,fx=3,fy=3,interpolation=cv2.INTER_NEAREST)

cv2.imwrite(sciezka_zapis, bayer_filter)

image = cv2.imread(sciezka_zapis)

cv2.imshow('bayer', bayer_filter)

kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv2.imshow('Identity', identity)
cv2.imwrite(zapis_identity, identity)

kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv2.imshow('Kernel Blur', img)
cv2.imwrite(zapis_kernel, img)

cv2.waitKey()
cv2.destroyAllWindows()