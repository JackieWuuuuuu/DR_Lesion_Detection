import os
import shutil
import random

# 设置文件夹路径
input_folder = r'C:\UltraLight-VMUNet-Output\1_mild_npdr\1_mild_npdr_256\1_mild_npdr_changename\1_mild_npdr_original'
output_train_folder = r'C:\PythonCode\ultralytics-main-pure\DR_noseg-cls\train\1_mild_npdr'
output_val_folder = r'C:\PythonCode\ultralytics-main-pure\DR_noseg-cls\val\1_mild_npdr'

# 创建输出文件夹
os.makedirs(output_train_folder, exist_ok=True)
os.makedirs(output_val_folder, exist_ok=True)

# 划分比例
train_ratio = 0.8

# 获取图片
images = os.listdir(input_folder)
random.shuffle(images)  # 随机

split_index = int(len(images) * train_ratio)

# 划分训练集和验证集
train_images = images[:split_index]
val_images = images[split_index:]

for image_name in train_images:
    shutil.copy(os.path.join(input_folder, image_name), os.path.join(output_train_folder, image_name))

for image_name in val_images:
    shutil.copy(os.path.join(input_folder, image_name), os.path.join(output_val_folder, image_name))

print("数据划分完成。")
