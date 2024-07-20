import napari
import tifffile
from glob import glob

import matplotlib.pyplot as plt
import tifffile
import numpy as np
from glob import glob

# 이미지 로드
# img = tifffile.imread("/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_best_model_output.tif")
# img = tifffile.imread("/data/no12neni/results/EGST39_A_Image2_30min/DataFolderIs_EGST39_A_Image2_30min_202406031252_ModelFolderIs_ATP_2D_best_model_demo/best_model/EGST39_A_Image2_30min_best_model_output.tif")

path = "/Users/gimchangheon/Documents/GitHub/DeepCAD-RT/result/ATP/EGST39_A_Image3_30min_best_model_output.tif"
img = tifffile.imread(path)
# 이미지 로드
# napari viewer로 시각화
viewer = napari.Viewer()
viewer.add_image(img, name='3D Image')

napari.run()
