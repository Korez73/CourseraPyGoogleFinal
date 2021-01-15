#!/usr/bin/env python3

#This script is step 1 on the final.
#Working with supplier images

from PIL import Image
import os

target_dir = r"C:\Repos\CourseraPyGoogleFinal\supplier-data\images"


def convert_images(dir):
    for filename in os.listdir(dir):
        
        source_path = os.path.join(dir, filename)
        #print(source_path)
        #print(os.path.splitext(filename))
        im = Image.open(source_path)
        im = im.convert("RGB").resize((600,400))
        fname, _ = os.path.splitext(filename)
        target_path = os.path.join(dir, fname) + ".jpeg"
        im.save(target_path, "jpeg")

if __name__ == "__main__":
    convert_images(target_dir)