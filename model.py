import torch.nn as nn
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights

class MobileNetV2Segmentation(nn.Module):
    def __init__(self, num_classes=3):
        super(MobileNetV2Segmentation, self).__init__()
        base_model = mobilenet_v2(weights=MobileNet_V2_Weights.DEFAULT)
        self.features = base_model.features
        
        # Lightweight decoder to map features back to pixel-level masks (224x224)
        self.decoder = nn.Sequential(
            nn.Conv2d(1280, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False),
            nn.Conv2d(256, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Upsample(scale_factor=16, mode='bilinear', align_corners=False),
            nn.Conv2d(128, num_classes, kernel_size=1)
        )
        
    def forward(self, x):
        x = self.features(x)
        x = self.decoder(x)
        return x

# Initialize model
segmentation_model = MobileNetV2Segmentation(num_classes=3)