#! /usr/bin/env python3

import os

BASEPATH_TEXT_DES = os.path.split(os.getcwd())[0] + "/assets/txtfiles/"
list_text_files = os.listdir(BASEPATH_TEXT_DES)

list = []
for text_file in list_text_files:
    with open(BASEPATH_TEXT_DES + text_file, 'r') as f:
        data = {"title": f.readline().rstrip("\n"),
                "name": f.readline().rstrip("\n"),
                "date": f.readline().rstrip("\n"),
                "description": f.readline().rstrip("\n")
                }
        list.append(data)

print(list)