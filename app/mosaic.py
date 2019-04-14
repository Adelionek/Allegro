
from __future__ import print_function
import requests
import os
from PIL import Image
arguments = {}
urls = []


def save_images():
    for i in range(arguments['ile']):
        url = requests.get(urls[i])
        with open('zdj_%d.jpeg' % i, 'wb') as f:
            f.write(url.content)




