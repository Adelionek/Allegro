import requests

arguments = {}
urls = []


def save_images():
    for i in range(arguments['ile']):
        url = requests.get(urls[i])
        with open('zdj_%d' % i, 'wb') as f:
            f.write(url.content)


    for url_address in urls:
        url = requests.get(url_address)
        with open('zdj_%d' % i, 'wb') as f:
            f.write(url.content)
