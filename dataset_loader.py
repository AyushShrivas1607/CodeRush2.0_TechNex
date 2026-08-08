import os
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import kagglehub

def load_spacecraft_dataset():
    """
    Downloads or retrieves the cached path of the spacecrafts dataset from Kaggle.
    """
    try:
        print("Synchronizing dataset from Kaggle...")
        path = kagglehub.dataset_download("dkudryavtsev/spacecrafts")
        print("Path to dataset files:", path)
        return path
    except Exception as e:
        print(f"Error downloading dataset from Kaggle: {e}")
        return None

class SpacecraftSegmentationDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        
        # Filter files to only keep images that have a verified matching mask
        all_images = sorted(os.listdir(image_dir))
        self.images = []
        
        for img_name in all_images:
            base_name, ext = os.path.splitext(img_name)
            mask_name = f"{base_name}_mask{ext}"
            mask_path = os.path.join(self.mask_dir, mask_name)
            
            if os.path.exists(mask_path):
                self.images.append(img_name)
                
        print(f"Verified dataset: {len(self.images)} valid image-mask pairs found out of {len(all_images)} total images.")
        
    def __len__(self):
        return len(self.images)
        
    def __getitem__(self, idx):
        img_name = self.images[idx]
        img_path = os.path.join(self.image_dir, img_name)
        
        base_name, ext = os.path.splitext(img_name)
        mask_name = f"{base_name}_mask{ext}"
        mask_path = os.path.join(self.mask_dir, mask_name)
        
        image = Image.open(img_path).convert("RGB")
        mask = Image.open(mask_path).convert("L") # Single-channel
        
        if self.transform:
            image = self.transform(image)
            
            # Resize mask using NEAREST interpolation to preserve class labels
            mask = mask.resize((224, 224), Image.Resampling.NEAREST)
            
            # Convert mask to numpy array
            mask_np = np.array(mask)
            
            # --- LABEL NORMALIZATION ---
            if mask_np.max() > 2:
                mask_np = (mask_np > 128).astype(np.int64) # Binary segmentation fallback (0 and 1)
            
            mask = torch.from_numpy(mask_np).long()
            
        return image, mask

# --- Define Transforms & Backend Integration Execution ---
if __name__ == "__main__":
    # Fetch dataset path dynamically via Kaggle cache/download manager
    dataset_path = load_spacecraft_dataset()
    
    if dataset_path:
        print("Dataset successfully synchronized. Ready to feed telemetry streams.")
        
        # Point paths dynamically to the downloaded Kaggle root directory
        # (Update folder subnames if your dataset directory layout maps differently)
        IMAGE_DIR = os.path.join(dataset_path, "images")
        MASK_DIR = os.path.join(dataset_path, "masks")

        train_transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        # Instantiate Dataset and DataLoader
        dataset = SpacecraftSegmentationDataset(image_dir=IMAGE_DIR, mask_dir=MASK_DIR, transform=train_transform)
        dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=2)

        print(f"DataLoader initialized successfully with {len(dataloader)} batches available.")