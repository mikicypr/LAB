import cv2
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt

path = r"C:\Users\mikol\OneDrive\Pulpit\Python\fft\do_kompresji\mond.jpg"
path_merged = r"C:\Users\mikol\OneDrive\Pulpit\Python\fft\do_kompresji\mond_compressed.jpg"
path_decompressed = r"C:\Users\mikol\OneDrive\Pulpit\Python\fft\do_kompresji\mond_decompressed.jpg"

img = imread(path)

plt.figure()
plt.imshow(img)
plt.axis('off')
plt.show()

img_channels = cv2.split(img)
merged_reconstructed = np.zeros_like(img)

keep = 1

for channel in range(3):
    img_channel = img_channels[channel]
    
    fourier = np.fft.fft2(img_channel)
    fourier_sort = np.sort(np.abs(fourier.reshape(-1)))

    thresh = fourier_sort[int(np.floor((1 - keep) * len(fourier_sort)))]
    ind = np.abs(fourier) > thresh
    Btlow = fourier * ind
    Alow = np.fft.ifft2(Btlow).real
    
    merged_reconstructed[:, :, channel] = Alow
    
plt.figure()
plt.imshow(merged_reconstructed)
plt.imsave(path_merged,merged_reconstructed)
plt.axis('off')
plt.title(f"{keep*100}% - Merged Image")
plt.show()

decompressed_img = np.zeros_like(img)

for channel in range(3):
    merged_channel = merged_reconstructed[:, :, channel]
    
    fft_merged = np.fft.fft2(merged_channel)
    fft_original = np.fft.fft2(img_channels[channel])
    
    merged_magnitude = np.abs(fft_merged)
    original_phase = np.angle(fft_original)
    
    reconstructed_fft = merged_magnitude * np.exp(1j * original_phase)
    reconstructed_channel = np.fft.ifft2(reconstructed_fft).real
    
    decompressed_img[:, :, channel] = reconstructed_channel

plt.figure()
plt.imshow(decompressed_img)
plt.imsave(path_decompressed, decompressed_img)
plt.axis('off')
plt.title("Decompressed Image")
plt.show()

mae=np.mean(np.abs(img-decompressed_img))/255

C=np.count_nonzero(merged_reconstructed)/(img.shape[0]*img.shape[1]*3)

print("MAE: ", np.round(mae,4))
print("C: ", np.round(C,4))
