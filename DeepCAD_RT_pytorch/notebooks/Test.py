from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation



import tifffile as tiff
import matplotlib.pyplot as plt

# Open the image file
img_path1 = '/data/no12neni/images/EGST39_A_Image 2_30min.tif'
img_path2 = '/data/no12neni/images/EGST_39_A_Image 3_30min.tif'
img_path2 = '/data/no12neni/datasets/fish_localbrain_demo/fish_localbrain.tif'




# Read the image data
img1 = tiff.imread(img_path1)
img2 = tiff.imread(img_path2)

# Select a specific time point (e.g., the first frame)
time_point = 100
slice_img1 = img1[time_point, :, :, :]
slice_img2 = img2[time_point, :, :, :]

# Display the selected time point
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('EGST39_A_Image 2_30min (Time Point 0)')
plt.imshow(slice_img1[0, :, :], cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('EGST_39_A_Image 3_30min (Time Point 0)')
plt.imshow(slice_img2[0, :, :], cmap='gray')
plt.axis('off')

plt.show()

# Create figure and axes
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Initialize the two image plots
im1 = ax[0].imshow(img1[0, 0, :, :], cmap='gray', animated=True)
ax[0].set_title('EGST39_A_Image 2_30min')
ax[0].axis('off')

im2 = ax[1].imshow(img2[0, 0, :, :], cmap='gray', animated=True)
ax[1].set_title('EGST_39_A_Image 3_30min')
ax[1].axis('off')

# Update function for animation
def update(frame):
    im1.set_array(img1[frame, 0, :, :])
    im2.set_array(img2[frame, 0, :, :])
    return [im1, im2]

# Create animation
ani = animation.FuncAnimation(fig, update, frames=min(img1.shape[0], img2.shape[0]), interval=50, blit=True)

plt.show()


# Calculate the mean intensity over time
mean_intensity_img1 = np.mean(img1, axis=(1, 2, 3))
mean_intensity_img2 = np.mean(img2, axis=(1, 2, 3))

# Plot the mean intensity over time
plt.figure(figsize=(10, 5))
plt.plot(mean_intensity_img1, label='EGST39_A_Image 2_30min')
plt.plot(mean_intensity_img2, label='EGST_39_A_Image 3_30min')
plt.xlabel('Time')
plt.ylabel('Mean Intensity')
plt.title('Mean Intensity Over Time')
plt.legend()
plt.show()
