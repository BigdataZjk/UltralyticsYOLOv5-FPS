# UltralyticsYOLOv5

**Author**: BigDataK

**StartTime**: 2023-08-04 00:28:00

**Description**: 一个Ultralytics的YOLOv5 SOTA模型,适用于类FPS游戏视觉处理和外设响应

**Note**: 基础环境部署详见 [https://jinke.love/uncategorized/15.html ,](https://jinke.love/machinelearning/15.html) ,每个机器环境部署有差异,onnx和engine模型建议自己导出

# 文件夹结构

[src](src)==src `项目代码文件夹`

* [main](src%2Fmain)                 `核心代码`

  * [datasets](src%2Fmain%2Fdatasets) `数据集,包括images和labels`
  * [functions](src%2Fmain%2Ffunctions) `功能函数`
  * [images](src%2Fmain%2Fimages) `各种图片图片`
  * [models](src%2Fmain%2Fmodels) `存模型或权重文件`
  * [my_tests](src%2Fmain%2Fmy_tests) `测试的地方`
  * --下面是文件
  * [detect.py](src%2Fmain%2Fdetect.py) `模型推理方法`
  * [export.py](src%2Fmain%2Fexport.py) `模型导出方法`
  * [main_run.py](src%2Fmain%2Fmain_run.py) `程序入口`
  * [requirements.txt](src%2Fmain%2Frequirements.txt) `项目依赖库配置文件`
  * [train.py](src%2Fmain%2Ftrain.py) `模型训练方法`
* 
* [resources](src%2Fresources)                 `资源文件`

  * [fonts](src%2Fresources%2Ffonts) `各种字体库文件`
  * [yolov5_libs](src%2Fresources%2Fyolov5_libs) `yolov5 GitHub源码`
