import os
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
from dataset_loader import SpacecraftSegmentationDataset, train_transform
from model import MobileNetV2Segmentation

def calculate_metrics(pred, target, num_classes=3):
    # Flatten tensors
    pred = pred.view(-1)
    target = target.view(-1)
    
    # Pixel Accuracy
    correct = (pred == target).sum().item()
    total = target.numel()
    pixel_acc = correct / max(1, total)
    
    # Intersection over Union (IoU) per class
    ious = []
    for cls in range(num_classes):
        pred_inds = (pred == cls)
        target_inds = (target == cls)
        
        intersection = (pred_inds & target_inds).sum().item()
        union = (pred_inds | target_inds).sum().item()
        
        if union == 0:
            ious.append(float('nan')) # Class not present in this sample
        else:
            ious.append(intersection / union)
            
    return pixel_acc, ious

def evaluate():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Paths (adjust if using a separate validation folder, using train dir as demo)
    VAL_IMG_DIR = r"D:\mobilenetv2\datasets\images\train"
    VAL_MASK_DIR = r"D:\mobilenetv2\datasets\mask\train"
    
    val_dataset = SpacecraftSegmentationDataset(VAL_IMG_DIR, VAL_MASK_DIR, transform=train_transform)
    valloader = DataLoader(val_dataset, batch_size=4, shuffle=False)
    
    # Load Model
    model = MobileNetV2Segmentation(num_classes=3).to(device)
    model.load_state_dict(torch.load("mobilenetv2_mission_segmentation.pth", map_location=device))
    model.eval()
    
    total_acc = 0.0
    class_ious = [[] for _ in range(3)]
    
    print("Evaluating model performance...")
    with torch.no_grad():
        for images, masks in tqdm(valloader):
            images, masks = images.to(device), masks.to(device)
            outputs = model(images)
            preds = torch.argmax(outputs, dim=1)
            
            for pred, mask in zip(preds, masks):
                acc, ious = calculate_metrics(pred, mask, num_classes=3)
                total_acc += acc
                for i, iou in enumerate(ious):
                    if not torch.isnan(torch.tensor(iou)):
                        class_ious[i].append(iou)
                        
    mean_acc = total_acc / len(val_dataset)
    mean_ious = [sum(ci)/len(ci) if ci else 0.0 for ci in class_ious]
    miou = sum(mean_ious) / len(mean_ious)
    
    print("\n--- Evaluation Results ---")
    print(f"Overall Pixel Accuracy: {mean_acc * 100:.2f}%")
    print(f"Mean IoU (mIoU): {miou * 100:.2f}%")
    for i, miou_cls in enumerate(mean_ious):
        print(f"Class {i} IoU: {miou_cls * 100:.2f}%")

if __name__ == "__main__":
    evaluate()