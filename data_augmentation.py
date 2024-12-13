import os
from torchvision import transforms
from PIL import Image

# 输入和输出文件夹路径
input_folder = r'C:\PythonCode\DGDR-main\GDRBench\images\IDRID\pdr'
output_folder = r'C:\PythonCode\ultralytics-main-pure\DR_cls_IDRiD\train\4_pdr'

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 数据增强
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),  # 随机水平翻转
    transforms.RandomRotation(30),  # 随机旋转
    transforms.Resize((224, 224)),  # 调整大小
])

# 获取所有图片
images = [f for f in os.listdir(input_folder) if f.endswith(('png', 'jpg', 'jpeg'))]

# 增强图片
count = 0
desired_count = 2000
num_augmentations_per_image = desired_count // len(images) + 1  # 每张图生成的增强数量

for image_name in images:
    image_path = os.path.join(input_folder, image_name)
    image = Image.open(image_path)

    for i in range(num_augmentations_per_image):  # 根据需要的数量生成增强图像
        augmented_image = transform(image)
        augmented_image.save(os.path.join(output_folder, f'aug_{count}.png'))
        count += 1

        if count >= desired_count:  # 达到2000张停止
            break
    if count >= desired_count:
        break

print("数据增强完成，生成的图片数量:", count)
