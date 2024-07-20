import os
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import tifffile

# List your directory names (adjust as needed)
directory_names = os.listdir("/data/no12neni/datasets/")
# Iterate through each directory
tif_file_list =[]
for dir_name in directory_names:
    # Construct path to the "best_model" subdirectory
    best_model_dir = "/data/no12neni/datasets/"+dir_name
    # Check if the "best_model" directory exists
    if os.path.exists(best_model_dir):
        # Find all .tif files within the "best_model" directory
        tif_files = glob(os.path.join(best_model_dir, "*.tif"))

        # Print the path of each found .tif file
        for tif_file in tif_files:
            print(tif_file)
            tif_file_list.append(tif_file)

# for tif_path in tif_file_list :
#     img = tifffile.imread(tif_path)
#     print(tif_path)
#     print(img.shape)
#     print()

# Create the directory if it doesn't exist
save_directory = "./image_original/t0"
os.makedirs(save_directory, exist_ok=True)
for tif_path in tif_file_list:
    img = tifffile.imread(tif_path)
    t = 0
    plt.imshow(img[t], cmap='gray')
    plot_title = 'original, t=0, ' + tif_path.split("/")[-1]
    plt.title(plot_title)
    plt.axis('off')
    save_path = os.path.join(save_directory, plot_title + ".png")
    plt.savefig(save_path)
    plt.show()
    plt.close()  # Close the figure

save_directory = "./image_original/max"
os.makedirs(save_directory, exist_ok=True)
for tif_path in tif_file_list:
    img = tifffile.imread(tif_path)
    print(img.shape, tif_path)
    max_projection = np.max(img, axis=0)
    plt.imshow(max_projection, cmap='gray')
    plot_title = 'original, max, ' + tif_path.split("/")[-1]
    plt.title(plot_title)
    plt.axis('off')
    save_path = os.path.join(save_directory, plot_title + ".png")
    plt.savefig(save_path)
    plt.show()
    plt.close()  # Close the figure