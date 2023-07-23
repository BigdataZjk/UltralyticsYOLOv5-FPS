import torch

# Images
img = '../images/sml.png'  # or file, Path, PIL, OpenCV, numpy, list
# # Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
# Custom Model
model = torch.hub.load(r'E:\GitProjects\yolov5', 'custom', path='../models/yolov5n.pt', source='local', device='0')

# Inference
results = model(img)

# Results
results.show()  # or .show(), .save(), .crop(), .pandas(), etc.
