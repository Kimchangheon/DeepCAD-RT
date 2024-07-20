import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import tifffile
import numpy as np
from glob import glob

# 이미지 로드
img = tifffile.imread("images/EGST_39_A_Image 3_30min.tif")

t=0
img_t = img[t]

# Assuming img_t is the 3D image array with shape (z_slices, height, width)
z_slices = img_t.shape[0]
rows = (z_slices + 3) // 4  # Calculate the number of rows needed

fig, axes = plt.subplots(rows, 4, figsize=(20, rows * 5))

for i in range(z_slices):
    row = i // 4
    col = i % 4
    axes[row, col].imshow(img_t[i], cmap='gray')
    axes[row, col].axis('off')
    axes[row, col].set_title(f'z = {i}')

# Turn off axes for any empty subplots
for j in range(z_slices, rows * 4):
    row = j // 4
    col = j % 4
    axes[row, col].axis('off')

plt.tight_layout()
plt.show()
