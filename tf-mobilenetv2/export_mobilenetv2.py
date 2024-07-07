import keras
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-o", required=True)
args = parser.parse_args()

model = keras.applications.MobileNet(weights="imagenet")
model.export(args.o)
