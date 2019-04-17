from flask import Flask, send_from_directory
import os

cwd = os.getcwd()

app = Flask(__name__)

from app import routes