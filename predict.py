import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
from model import MobileNetV2Segmentation

def run_inference(image_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # 1. Load Model and Weights
    model = MobileNetV2Segmentation(num_classes=3).to(device)
    model.load_state_dict(torch.load("mobilenetv2_mission_segmentation.pth", map_location=device))
    model.eval()
    
    # 2. Preprocess Image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    original_image = Image.open(image_path).convert("RGB")
    input_tensor = transform(original_image).unsqueeze(0).to(device) # Add batch dimension
    
    # 3. Predict
    with torch.no_grad():
        output = model(input_tensor)
        prediction = torch.argmax(output, dim=1).squeeze(0).cpu().numpy()
        
    print("Inference completed successfully!")
    print(f"Predicted mask shape: {prediction.shape}")
    
    # 4. Visualize Results
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original_image.resize((224, 224)))
    
    plt.subplot(1, 2, 2)
    plt.title("Predicted Segmentation Mask")
    plt.imshow(prediction, cmap="gray")
    plt.show()

if __name__ == "__main__":
    # Test on a sample image from your validation or training set
    sample_img = r"D:/mobilenetv2/datasets/images/train/img_resize_0.png"
    run_inference(sample_img)