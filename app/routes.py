from app import app
from flask import request, render_template


@app.route('/')
def base_page():
    return "Hello"


@app.route('/mozaika')
def mozaika():

    arguments = {}
    urls = []
    if request.args.get('losowo') is not None:
        randomly = request.args.get('losowo')
        arguments['losowo'] = randomly
    if request.args.get('rozdzielczosc') is not None:
        resolution = request.args.get('rozdzielczosc')
        resolution_args = resolution.split("x")
        arguments['X'] = resolution_args[0]
        arguments['Y'] = resolution_args[1]

    images = request.args.get('zdjecia')
    urls.append(images)


    return render_template('base.html', arguments=arguments, urls=urls)
