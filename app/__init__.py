from flask import Flask, send_from_directory
import os

cwd = os.getcwd()

app = Flask(__name__)
app._static_folder = os.path.join('C:\\Users\\PC\\Documents\\Git\\Allegro\\static')


from app import routes