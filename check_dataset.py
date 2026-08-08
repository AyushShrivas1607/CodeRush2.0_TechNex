import os
from dataset_loader import SpacecraftSegmentationDataset, train_transform

# Updated with your exact absolute paths
TRAIN_IMG_DIR = r"D:\mobilenetv2\datasets\images\train"
TRAIN_MASK_DIR = r"D:\mobilenetv2\datasets\mask\train"

print("Checking dataset paths...")
print(f"Image directory exists: {os.path.exists(TRAIN_IMG_DIR)}")
print(f"Mask directory exists: {os.path.exists(TRAIN_MASK_DIR)}")

if os.path.exists(TRAIN_IMG_DIR) and os.path.exists(TRAIN_MASK_DIR):
    dataset = SpacecraftSegmentationDataset(TRAIN_IMG_DIR, TRAIN_MASK_DIR, transform=train_transform)
    print(f"Total images found in training set: {len(dataset)}")
    
    if len(dataset) > 0:
        # Try fetching the first sample
        img, mask = dataset[0]
        print("Success! First sample loaded correctly.")
        print(f"Image tensor shape: {img.shape}")
        print(f"Mask tensor shape: {mask.shape}")
    else:
        print("Warning: The image directory is empty. Add your image files there.")
else:
    print("Error: Directory paths do not match. Double-check your folder structure.")