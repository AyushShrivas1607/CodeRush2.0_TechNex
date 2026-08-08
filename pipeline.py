import os
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from model import MobileNetV2Segmentation

class MissionPipeline:
    def __init__(self, weights_path="mobilenetv2_mission_segmentation.pth", num_classes=3):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Initializing Mission Pipeline on device: {self.device}")
        
        # Load Model
        self.model = MobileNetV2Segmentation(num_classes=num_classes).to(self.device)
        self.model.load_state_dict(torch.load(weights_path, map_location=self.device))
        self.model.eval()
        
        # Preprocessing Transform
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def process_frame(self, image_path, anomaly_class_index=2, threshold_ratio=0.05):
        """
        Processes a single frame, runs segmentation, and checks for critical structural anomalies.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Frame not found: {image_path}")
            
        original_image = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(original_image).unsqueeze(0).to(self.device)
        
        with torch.no_grad():
            output = self.model(input_tensor)
            prediction = torch.argmax(output, dim=1).squeeze(0).cpu().numpy()
            
        # Calculate anomaly metric (e.g., ratio of pixels belonging to a fault/damage class)
        total_pixels = prediction.size
        anomaly_pixels = np.sum(prediction == anomaly_class_index)
        anomaly_ratio = anomaly_pixels / total_pixels
        
        # Decision State Machine Trigger
        status = "NOMINAL"
        action = "CONTINUE_MONITORING"
        
        if anomaly_ratio > threshold_ratio:
            status = "DEGRADED_ANOMALY_DETECTED"
            action = "EXECUTE_CORRECTIVE_ACTION_PROTOCOL"
            
        report = {
            "image": os.path.basename(image_path),
            "status": status,
            "anomaly_pixel_ratio": float(anomaly_ratio),
            "recommended_action": action
        }
        
        return report

if __name__ == "__main__":
    pipeline = MissionPipeline()
    
    # Simulate processing a live incoming feed frame
    test_frame = r"D:\mobilenetv2\datasets\images\train\img_resize_0.png"
    
    print(f"\nProcessing telemetry frame: {os.path.basename(test_frame)}...")
    telemetry_report = pipeline.process_frame(test_frame)
    
    print("\n--- Mission Telemetry Report ---")
    for key, value in telemetry_report.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")