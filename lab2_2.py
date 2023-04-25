import cv2
import numpy as np

path=r"C:\Users\Johny017\Desktop\zdj\original.jpg"
sciezka_zapis=r"C:\Users\Johny017\Desktop\zdj\kwiaty_szum_256.jpg"
zapis_identity=r"C:\Users\Johny017\Desktop\zdj\kwiaty_identity_1_256.jpg"
zapis_kernel=r"C:\Users\Johny017\Desktop\zdj\kwiaty_blur_256.jpg"

img = cv2.imread(path)

val_lambda=256

img_szum = np.random.poisson(img/img.max()*val_lambda)/val_lambda

img_szum=np.clip(img_szum*255,0,255).astype(np.uint8)

cv2.imshow('original',img)
cv2.imshow('szum', img_szum)
cv2.imwrite(sciezka_zapis,img_szum)


kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(src=img_szum, ddepth=-1, kernel=kernel1)

kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=img_szum, ddepth=-1, kernel=kernel2)

cv2.imshow('Kernel Blur', img)
cv2.imwrite(zapis_kernel, img)

cv2.imshow('Identity', identity)
cv2.imwrite(zapis_identity, identity)

cv2.waitKey(0)
cv2.destroyAllWindows()
