import os
import tifffile
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

# dir_list = ['DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031310_ModelFolderIs_ATP_3D_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031328_ModelFolderIs_NP_2D_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031345_ModelFolderIs_NP_3D_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031403_ModelFolderIs_drosophila_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031421_ModelFolderIs_fish_localbrain_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031439_ModelFolderIs_fish_wholebrain_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031456_ModelFolderIs_mouse_spine_best_model_demo',
# 'DataFolderIs_EGST39_A_Image2_30min_202406031514_ModelFolderIs_simulate_-2.51dBSNR_1000frames_best_model_demo']
#
# new_dir_list = []
# for path in dir_list :
#     new_dir_path = os.path.join('/data/no12neni/results/EGST39_A_Image2_30min',path)
#     new_dir_path = os.path.join(new_dir_path,'best_model')
#     new_dir_list.append(new_dir_path)

# from z0 to z19
# Let's first see z=7'

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

# plot all z=10
# fig, axes = plt.subplots(3, 3, figsize=(15, 15))
# for idx, dir_path in enumerate(new_dir_list):
#     z = 10
#     file_name = f'EGST39_A_Image2_30min_z{z}_best_model_output.tif'
#     img = tifffile.imread(os.path.join(dir_path, file_name))
#     t =0
#     img = img[t]
#     row, col = divmod(idx, 3)
#     axes[row, col].imshow(img, cmap='gray')
#     axes[row, col].axis('off')
#     axes[row, col].set_title(f't=0,z=10,Denosied by {dir_path.split("ModelFolderIs_")[1].split("_best_model_")[0]}')
#
# plt.tight_layout()
# plt.show()

# for dir_path in new_dir_list :
#     stacked_images = np.zeros((342, 20, 538, 545), dtype=np.float32)
#     for i in range(20) :
#         file_name = 'EGST39_A_Image2_30min_z'+str(i)+'_best_model_output.tif'
#         img = tifffile.imread(os.path.join(dir_path,file_name))
#         stacked_images[:, i, :, :] = img
#     print(img.shape)
#     # Save the final stacked image
#     output_file_name = 'EGST39_A_Image2_30min_best_model_output.tif'
#     output_file_path = os.path.join(dir_path, output_file_name)
#     tifffile.imwrite(output_file_path, stacked_images)
#     # Assuming img_t is the 3D image array with shape (z_slices, height, width)
#     img_t = stacked_images[0]
#     z_slices = img_t.shape[0]
#     rows = (z_slices + 3) // 4  # Calculate the number of rows needed
#
#     fig, axes = plt.subplots(rows, 4, figsize=(20, rows * 5))
#
#     for i in range(z_slices):
#         row = i // 4
#         col = i % 4
#         axes[row, col].imshow(img_t[i], cmap='gray')
#         axes[row, col].axis('off')
#         axes[row, col].set_title(f'z = {i}')
#
#     # Turn off axes for any empty subplots
#     for j in range(z_slices, rows * 4):
#         row = j // 4
#         col = j % 4
#         axes[row, col].axis('off')
#
#     plt.tight_layout()
#
#     # Save the figure
#     fig_file_name = 't=0.png'
#     fig_file_path = os.path.join(dir_path, fig_file_name)
#     plt.savefig(fig_file_path, bbox_inches='tight')
#
#     print(f'Figure saved to {fig_file_path}')
#     plt.show()

dir_list =['DataFolderIs_EGST39_A_Image3_30min_202406031303_ModelFolderIs_ATP_2D_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031321_ModelFolderIs_ATP_3D_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031339_ModelFolderIs_NP_2D_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031357_ModelFolderIs_NP_3D_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031414_ModelFolderIs_drosophila_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031432_ModelFolderIs_fish_localbrain_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031450_ModelFolderIs_fish_wholebrain_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031508_ModelFolderIs_mouse_spine_best_model_demo',
'DataFolderIs_EGST39_A_Image3_30min_202406031525_ModelFolderIs_simulate_-2.51dBSNR_1000frames_best_model_demo']


new_dir_list = []
for path in dir_list :
    new_dir_path = os.path.join('/data/no12neni/results/EGST39_A_Image3_30min',path)
    new_dir_path = os.path.join(new_dir_path,'best_model')
    new_dir_list.append(new_dir_path)
#
# for dir_path in new_dir_list :
#     stacked_images = np.zeros((237,19,532,538), dtype=np.float32)
#     for i in range(19) :
#         file_name = 'EGST39_A_Image3_30min_z'+str(i)+'_best_model_output.tif'
#         img = tifffile.imread(os.path.join(dir_path,file_name))
#         stacked_images[:, i, :, :] = img
#     print(img.shape)
#     # Save the final stacked image
#     output_file_name = 'EGST39_A_Image3_30min_best_model_output.tif'
#     output_file_path = os.path.join(dir_path, output_file_name)
#     tifffile.imwrite(output_file_path, stacked_images)
#     # Assuming img_t is the 3D image array with shape (z_slices, height, width)
#     img_t = stacked_images[0]
#     z_slices = img_t.shape[0]
#     rows = (z_slices + 3) // 4  # Calculate the number of rows needed
#
#     fig, axes = plt.subplots(rows, 4, figsize=(20, rows * 5))
#
#     for i in range(z_slices):
#         row = i // 4
#         col = i % 4
#         axes[row, col].imshow(img_t[i], cmap='gray')
#         axes[row, col].axis('off')
#         axes[row, col].set_title(f'z = {i}')
#
#     # Turn off axes for any empty subplots
#     for j in range(z_slices, rows * 4):
#         row = j // 4
#         col = j % 4
#         axes[row, col].axis('off')
#
#     plt.tight_layout()
#
#     # Save the figure
#     fig_file_name = 't=0.png'
#     fig_file_path = os.path.join(dir_path, fig_file_name)
#     plt.savefig(fig_file_path, bbox_inches='tight')
#
#     print(f'Figure saved to {fig_file_path}')
#     plt.show()

# plot all z=0
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
for idx, dir_path in enumerate(new_dir_list):
    z = 0
    file_name = f'EGST39_A_Image3_30min_z{z}_best_model_output.tif'
    img = tifffile.imread(os.path.join(dir_path, file_name))
    t =0
    img = img[t]
    row, col = divmod(idx, 3)
    axes[row, col].imshow(img, cmap='gray')
    axes[row, col].axis('off')
    axes[row, col].set_title(f't=0,z=10,Denosied by {dir_path.split("ModelFolderIs_")[1].split("_best_model_")[0]}')

plt.tight_layout()
plt.show()

['/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z5_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z10_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z3_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z17_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z6_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z9_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z19_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z0_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z16_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z8_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z15_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z2_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z12_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z14_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z13_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z1_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z7_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z18_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z11_best_model_output.tif',
 '/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_z4_best_model_output.tif']