import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the images
img_path1 = '/data/no12neni/images/EGST39_A_Image 2_30min.tif'
img_path2 = '/data/no12neni/images/EGST_39_A_Image 3_30min.tif'

image1 = Image.open(img_path1)
image2 = Image.open(img_path2)

# Convert images to numpy arrays for easier manipulation if needed
image1_array = np.array(image1)
image2_array = np.array(image2)

# Plot the images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image1_array, cmap='gray')
axes[0].set_title('Image 1')

axes[1].imshow(image2_array, cmap='gray')
axes[1].set_title('Image 2')

plt.show()
