import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset_loader import SpacecraftSegmentationDataset, train_transform
from model import MobileNetV2Segmentation

def train_model():
    # Updated with your exact absolute paths
    TRAIN_IMG_DIR = r"D:\mobilenetv2\datasets\images\train"
    TRAIN_MASK_DIR = r"D:\mobilenetv2\datasets\mask\train"
    
    # 1. Verify paths and initialize DataLoader
    if not os.path.exists(TRAIN_IMG_DIR) or not os.path.exists(TRAIN_MASK_DIR):
        print(f"Error: Dataset directories not found.\nImage Path: {TRAIN_IMG_DIR}\nMask Path: {TRAIN_MASK_DIR}")
        return

    train_dataset = SpacecraftSegmentationDataset(TRAIN_IMG_DIR, TRAIN_MASK_DIR, transform=train_transform)
    
    if len(train_dataset) == 0:
        print("Error: No training images found in the specified directory.")
        return
        
    trainloader = DataLoader(train_dataset, batch_size=4, shuffle=True)
    print(f"Dataset successfully loaded with {len(train_dataset)} samples.")

    # 2. Model, Loss, and Optimizer
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = MobileNetV2Segmentation(num_classes=3).to(device)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # 3. Training Loop
    epochs = 3
    model.train()
    
    print(f"Starting training on device: {device}")
    for epoch in range(epochs):
        epoch_loss = 0.0
        for images, masks in trainloader:
            images, masks = images.to(device), masks.to(device)
            
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, masks)
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()
            
        print(f"Epoch [{epoch+1}/{epochs}] | Loss: {epoch_loss / max(1, len(trainloader)):.4f}")

    # Save trained weights
    torch.save(model.state_dict(), "mobilenetv2_mission_segmentation.pth")
    print("Model training complete and weights saved to 'mobilenetv2_mission_segmentation.pth'.")

if __name__ == "__main__":
    train_model()