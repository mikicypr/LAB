import cv2
import numpy as np

path = r"C:\Users\mikol\OneDrive\Pulpit\Python\fft\do_kompresji\mond.jpg"
path_compressed = r"C:\Users\mikol\OneDrive\Pulpit\Python\fft\do_kompresji\mond_compressed.jpg"
path_decompressed = r"C:\Users\mikol\OneDrive\Pulpit\Python\fft\do_kompresji\mond_decompressed.jpg"

img = cv2.imread(path)

img_channels = cv2.split(img)
compressed_reconstructed = np.zeros_like(img)

keep = 1

for channel in range(3):
    img_channel = img_channels[channel]

    img_dct = cv2.dct(np.float32(img_channel))

    thresh = np.percentile(np.abs(img_dct), (1-keep) * 100)

    img_dct_compressed = img_dct * (np.abs(img_dct) > thresh)

    img_reconstructed = cv2.idct(img_dct_compressed)

    compressed_reconstructed[:, :, channel] = img_reconstructed

cv2.imshow('Compressed Image', compressed_reconstructed)
cv2.imwrite(path_compressed, compressed_reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()

decompressed_img = np.zeros_like(img)

for channel in range(3):
    compressed_channel = compressed_reconstructed[:, :, channel]

    compressed_dct = cv2.dct(np.float32(compressed_channel))

    decompressed_channel = cv2.idct(compressed_dct)

    decompressed_img[:, :, channel] = decompressed_channel

cv2.imshow('Decompressed Image', decompressed_img)
cv2.imwrite(path_decompressed, decompressed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

mae=np.mean(np.abs(img-decompressed_img))/255

C=np.count_nonzero(compressed_reconstructed)/(img.shape[0]*img.shape[1]*3)

print("MAE: ", np.round(mae,4))
print("C: ", np.round(C,4))