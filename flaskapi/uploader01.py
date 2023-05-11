#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/uploader", methods = ["GET" , "POST"]
def upload_file():

