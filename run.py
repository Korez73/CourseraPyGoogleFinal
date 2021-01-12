#!/usr/bin/env python3
import os
import requests
import json

#This script is step 3 on the final.
#Uploading the descriptions

target_dir = r"C:\Repos\CourseraPyGoogleFinal\supplier-data\descriptions"


def read_files(dir):

    all_image_data = []

    for filename in os.listdir(dir):
        if not filename.endswith(".txt"):
            continue

        source_path = os.path.join(dir, filename)
        with open(source_path, 'r') as opened:
            lines = opened.read().splitlines()
            opened.close()

            image_data = ImageData()
            image_data.name = lines[0]
            image_data.image_name = image_data.name + ".jpeg"
            image_data.weight = int(lines[1].replace('lbs',''))
            image_data.description = lines[2]
            print(image_data)
            all_image_data.append(image_data)
            
    return all_image_data


def post_data(json):
    response = requests.post("http://34.70.200.201", data=json)
    response.raise_for_status()


class ImageData:
    name = None
    weight = None
    description = None
    image_name = None

    def __str__(self):
        results = "Name:{}\n".format(self.name)
        results += "Weight:{}\n".format(self.weight)
        results += "Image Name:{}\n".format(self.image_name)
        results += "Description:{}\n".format(self.description)
        return results


if __name__ == "__main__":
    
    data = read_files(target_dir)
    
    for d in data:
        json_data = json.dumps(d.__dict__)
        print(json_data)

    # for fb in fbacks:
    #     post_feedback(fb)