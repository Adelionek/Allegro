from app import app, mosaic
from flask import request, render_template


@app.route('/')
def base_page():
    return "Hello"


@app.route('/mozaika')
def mozaika():
    if request.args.get('losowo') is not None:
        randomly = request.args.get('losowo')
        mosaic.arguments['losowo'] = randomly
    if request.args.get('rozdzielczosc') is not None:
        resolution = request.args.get('rozdzielczosc')
        resolution_args = resolution.split("x")
        mosaic.arguments['X'] = resolution_args[0]
        mosaic.arguments['Y'] = resolution_args[1]
    else:
        mosaic.arguments['X'] = 2048
        mosaic.arguments['Y'] = 2048

    images = request.args.get('zdjecia')
    if images is None:
        mosaic.arguments['ile'] = 0
        return render_template('errorpage.html', ile=mosaic.arguments['ile'])

    mosaic.urls = images.split(',')
    mosaic.arguments['ile'] = len(mosaic.urls)

    if(mosaic.arguments['ile']) > 8:
        return render_template('errorpage.html', ile=mosaic.arguments['ile'])

    mosaic.save_images()

    return render_template('base.html', arguments=mosaic.arguments, urls=mosaic.urls)
