import cv2
import numpy as np

path=r"C:\Users\mikol\OneDrive\Pulpit\Python\pobrane (1).jpg"
zapis_wiekszy=r"C:\Users\mikol\OneDrive\Pulpit\Python\obraz_powiekszony.jpg"
zapis_mniejszy=r"C:\Users\mikol\OneDrive\Pulpit\Python\obraz_pomniejszony.jpg"

img = cv2.imread(path)


skala = 2
width = int(img.shape[1] * skala)
height = int(img.shape[0] * skala)
wymiar = (width, height)
wiekszy = cv2.resize(img, wymiar, interpolation = cv2.INTER_NEAREST)


skala_zmniejsz = 2
width = int(img.shape[1] * 1/skala_zmniejsz)
height = int(img.shape[0] * 1/skala_zmniejsz)
wymiar = (width, height)
mniejszy = cv2.resize(img, wymiar, interpolation = cv2.INTER_NEAREST)


cv2.imshow('Originalny', img)
cv2.imshow('Wiekszy', wiekszy)
cv2.imwrite(zapis_wiekszy,wiekszy)
cv2.imshow('Mniejszy', mniejszy)
cv2.imwrite(zapis_mniejszy,mniejszy)
cv2.waitKey(0)
cv2.destroyAllWindows()
