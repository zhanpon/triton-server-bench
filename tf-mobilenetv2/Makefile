MODEL_PATH = models/mobilenetv2/1/model.savedmodel

build: $(MODEL_PATH)

$(MODEL_PATH):
	../.venv/bin/python export_mobilenetv2.py -o $@
