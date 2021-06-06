#! /usr/bin/env python3

import os
import requests

BASEPATH_TEXT_DES = os.path.split(os.getcwd())[0] + "/assets/txtfiles/"
list_text_files = os.listdir(BASEPATH_TEXT_DES)

BASEPATH_IMAGE = os.path.split(os.getcwd())[0] + "/assets/images/"
list_image_files = os.listdir(BASEPATH_IMAGE)
list_images = [image_name for image_name in list_image_files if '.jpeg' in image_name]

list = []
for text_file in list_text_files:
    with open(BASEPATH_TEXT_DES + text_file, 'r') as f:
        data = {"title": f.readline().rstrip("\n"),
                "name": f.readline().rstrip("\n"),
                "date": f.readline().rstrip("\n"),
                "description": f.readline().rstrip("\n")
                }

        for image_file in list_images:
            if image_file.split('.')[0] in text_file.split('.')[0]:
                data['image_name'] = image_file

        list.append(data)

for item in list:
    resp = requests.post('http://localhost/articles/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))
