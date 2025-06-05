import os
from torchvision import transforms
from PIL import Image

# 输入和输出文件夹路径
input_folder = r'A'
output_folder = r'B'

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),  # 随机水平翻转
    transforms.RandomRotation(30),  # 随机旋转
    transforms.Resize((224, 224)),  # 调整大小
])

# 获取图片
images = [f for f in os.listdir(input_folder) if f.endswith(('png', 'jpg', 'jpeg'))]

# 增强
count = 0
desired_count = 2000
num_augmentations_per_image = desired_count // len(images) + 1  

for image_name in images:
    image_path = os.path.join(input_folder, image_name)
    image = Image.open(image_path)

    for i in range(num_augmentations_per_image):  
        augmented_image = transform(image)
        augmented_image.save(os.path.join(output_folder, f'aug_{count}.png'))
        count += 1

        if count >= desired_count:  
            break
    if count >= desired_count:
        break

print("生成图片数量:", count)
