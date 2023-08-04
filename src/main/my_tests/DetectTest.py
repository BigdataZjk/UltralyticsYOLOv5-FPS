# import torch
#
# # Images
# img = '../images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
# # # Model
# # model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
# # Custom Model
# model = torch.hub.load(r'E:\GitProjects\UltralyticsYOLOv5\src\resources\yolov5_libs', 'custom', path='../models/yolov5s.engine', source='local', device='0')
#
# # Inference
# results = model(img)
#
# # Results
# results.show()  # or .show(), .save(), .crop(), .pandas(), etc.

import torch
import cv2
from PIL import Image

# 读取图像
img_path = '../images/zidane.jpg'
img = cv2.imread(img_path)
# 调整图像大小并将其转换为 PyTorch 张量
resized_img = cv2.resize(img, (640, 640))  # 将图像大小调整为 (640, 640)
tensor_img = torch.from_numpy(resized_img).permute(2, 0, 1).unsqueeze(0).float() / 255.0

# 加载模型
model = torch.hub.load(r'E:\GitProjects\UltralyticsYOLOv5\src\resources\yolov5_libs', 'custom', path='../models/yolov5s.engine', source='local', force_reload=True)

# 进行推理
results = model(tensor_img)

# 将结果绘制在原始图像上
img = Image.open(img_path)
img = results.pred.render(img)

# 打印检测到的目标信息
for i, det in enumerate(results[0].xyxy):
    print(f"{i}: {results.names[int(det[5])]} ({det[4]:.2f})")

# 显示图像
img.show()