import torch
import torch.nn as nn
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights

# 1. Image Transformations (Resized to 224x224 for MobileNetV2 compatibility)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

# 2. Load Space Mission Component Datasets
trainset = ImageFolder(root="./dataset/train", transform=transform)
testset = ImageFolder(root="./dataset/val", transform=transform)

trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
testloader = DataLoader(testset, batch_size=64)

# 3. Build MobileNetV2 (Pretrained Feature Extractor + Custom Mission Classifier)
model = mobilenet_v2(weights=MobileNet_V2_Weights.DEFAULT)

# Freeze feature extractor layers for secure transfer learning
for param in model.parameters():
    param.requires_grad = False

# Replace final layer to match mission component categories (e.g., 3 classes)
num_classes = 3
model.classifier[1] = nn.Linear(model.last_channel, num_classes)

criterion = nn.CrossEntropyLoss()
# Optimize only the classifier parameters since base layers are frozen
optimizer = optim.Adam(model.classifier.parameters(), lr=0.001)

# 4. Training Loop for Mission Component Verification
epochs = 5

for epoch in range(epochs):
    epoch_training_loss = 0.0
    model.train()

    for images, labels in trainloader:
        optimizer.zero_grad()
        
        output = model(images) # Forward Pass
        loss = criterion(output, labels) # Loss function
        loss.backward() # Backward Pass
        optimizer.step() # Update parameters

        epoch_training_loss += loss.item()

    print(f"epoch={epoch+1}/{epochs} & loss={epoch_training_loss/len(trainloader)}")

# 5. Evaluation Loop
correct_labels = 0
total_labels = 0

model.eval()

with torch.no_grad():
    for images, labels in testloader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        correct_labels += (predicted == labels).sum().item()
        total_labels += labels.size(0)

print(f"accuracy = {correct_labels / total_labels * 100:.2f}%")