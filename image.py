#!/usr/bin python3

from PIL import Image
import os

directory = "images/"
output_dir = "opt/icons/"

for filename in os.listdir(directory):
	if filename != ".DS_Store":
		img = Image.open(os.path.join(directory,filename))
		img = img.rotate(-90)
		img = img.resize((128,128))
		img = img.convert("RGB")
		img.save(os.path.join(output_dir,filename+".jpeg"))