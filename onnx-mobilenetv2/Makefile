MODEL_URL = https://github.com/onnx/models/raw/main/validated/vision/classification/mobilenet/model/mobilenetv2-12.onnx
ONNX_PATH = models/mobilenetv2/1/model.onnx 


build: $(ONNX_PATH)

$(ONNX_PATH):
	wget -O $@ $(MODEL_URL)

