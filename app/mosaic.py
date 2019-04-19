import math
import requests
import os
from PIL import Image
from random import shuffle

arguments = {}
urls = []
cwd = os.getcwd()
result_path = os.path.join(cwd, 'app', 'static', 'result_photo.jpeg')


def save_images():
    print(arguments['losowo'])

    if arguments['losowo'] == '1':
        print('dziala')
        shuffle(urls)

    for i in range(arguments['ile']):
        url = requests.get(urls[i])
        with open(os.path.join(cwd, 'app', 'static', 'temp', 'zdj_%d.jpeg' % i), 'wb') as f:
            f.write(url.content)


def mozaika():
    files = []

    for r, d, f in os.walk(os.path.join(cwd, 'app', 'static', 'temp')):
        for file in f:
            files.append(os.path.join(r, file))

    ile = len(files)
    size = (int(arguments['X']), int(arguments['Y']))
    result = Image.new("RGB", size)

    for index, file in enumerate(files):
        path = os.path.expanduser(file)
        img = Image.open(path)
        width = int(size[0]/2)
        height = int(size[1]/(math.ceil(ile/2)))
        print(width)
        print(height)

        resized = img.resize((width, height), Image.ANTIALIAS)
        if ile % 2 == 1 and index == ile-1:
            width = int(size[0])
            resized = img.resize((size[0], height), Image.ANTIALIAS)
        print(resized.size)
        x = index % 2 * width
        y = index//2 * height
        print('pos {0},{1} size {2},{3}'.format(x, y, width, height))
        result.paste(resized, (x, y, x + width, y + height))

    result.save(result_path)
    print(result_path)
    print(ile)


def delete_temp_files():
    folder = os.path.join(cwd, 'app', 'static')
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
