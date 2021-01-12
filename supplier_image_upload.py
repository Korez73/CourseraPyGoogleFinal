#!/usr/bin/env python3
import requests
import os

#This script is step 2 on the final.
#uploading images to web server

url = "http://localhost/upload/"
target_dir = r"C:\Repos\CourseraPyGoogleFinal\supplier-data\images"

def upload_images(dir):
    for filename in os.listdir(dir):
        if not filename.endswith(".jpeg"):
            continue

        source_path = os.path.join(dir, filename)
        with open(source_path, 'rb') as opened:
            try:
                r = requests.post(url, files={'file':opened})
            except:
                print("error posting to localhost")


if __name__ == "__main__":
    upload_images(target_dir)