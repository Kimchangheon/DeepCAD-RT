import tifffile as tiff
import os

# Define the paths to the images
img_path1 = '../EGST39_A_Image 2_30min.tif'
img_path2 = '../EGST_39_A_Image 3_30min.tif'

# Read the images
img1 = tiff.imread(img_path1)
img2 = tiff.imread(img_path2)

# Create output directories if they don't exist
output_dir1 = 'EGST39_A_Image2_30min'
output_dir2 = 'EGST39_A_Image3_30min'
os.makedirs(output_dir1, exist_ok=True)
os.makedirs(output_dir2, exist_ok=True)

# Save Z-axis slices for img1
for z in range(img1.shape[1]):
    slice_img = img1[:, z, :, :]
    output_path = os.path.join(output_dir1, f'EGST39_A_Image2_30min_z{z}.tif')
    tiff.imwrite(output_path, slice_img)

# Save Z-axis slices for img2
for z in range(img2.shape[1]):
    slice_img = img2[:, z, :, :]
    output_path = os.path.join(output_dir2, f'EGST39_A_Image3_30min_z{z}.tif')
    tiff.imwrite(output_path, slice_img)

print("Z-axis slices have been saved successfully.")
