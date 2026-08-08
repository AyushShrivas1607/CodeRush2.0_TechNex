import os

image_dir = r"D:/mobilenetv2/datasets/images/train"
mask_dir = r"D:/mobilenetv2/datasets/mask/train"

images = sorted(os.listdir(image_dir))[:5]
masks = sorted(os.listdir(mask_dir))[:5]

print("First 5 images:", images)
print("First 5 masks: ", masks)