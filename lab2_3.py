import numpy as np
import cv2
from scipy.ndimage import gaussian_filter
from skimage import restoration
import matplotlib.pyplot as plt
import matplotlib.image as mplt

path=r"C:\Users\Johny017\Desktop\zdj\L2.3\Original.jpg"
sciezka_zapisu_szum=r"C:\Users\Johny017\Desktop\zdj\L2.3\Original_1.jpg"
sciezka_zapisu=r"C:\Users\Johny017\Desktop\zdj\L2.3\Original_2.jpg"


img = cv2.imread(path)
cv2.imshow('Original',img)
val_lambda=1
img_szum = np.random.poisson(img/img.max()*val_lambda)/val_lambda
img_szum=np.clip(img_szum*255,0,255).astype(np.uint8)

cv2.imshow('Szum',img_szum)
cv2.imwrite(sciezka_zapisu_szum, img_szum)

def anascombe(x):
    return 2*np.sqrt(x+3/8)

def reverse_anascombe(x):
    return (x/2)**2-3/8

im_anscombe=anascombe(img_szum)
#cv2.imshow('Anscombe',im_anscombe)

#im_smooth_1=restoration.denoise_tv_chambolle(im_anscombe)
#im_smooth_1=restoration.denoise_bilateral(im_anscombe,channel_axis=-1)
im_smooth_1=gaussian_filter(im_anscombe, 2, mode='nearest')
#cv2.imshow('Smooth 1',im_smooth_1)

im_unanscombe_1=reverse_anascombe(im_smooth_1)
cv2.imshow('Unanscombe 1',im_unanscombe_1)
cv2.imwrite(sciezka_zapisu, im_unanscombe_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
