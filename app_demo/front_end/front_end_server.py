# -*- coding: utf-8 -*-
import os
import io
import sys
import time
from flask import Flask, request, flash, render_template, jsonify, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import requests
import glob

front_server_url = "0.0.0.0"

port = '8891'

back_server_url = 'http://localhost:8892/'

dir_ = os.getcwd()

UPLOAD_FOLDER = 'back_end/Data_input/'
UPLOAD_FOLDER = os.path.join(dir_,UPLOAD_FOLDER)
print('path : ', UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 2

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict(back_route, return_page):
   
    files=glob.glob(UPLOAD_FOLDER+"/*.*")
    for f in files:
        os.remove(f)
    if request.method == 'POST':
    # check if the post request has the file part
        if 'inputExcel' not in request.files:
            message = 'No file part'
            return render_template('predict_error.html', message=message)

        url_back_predict = back_server_url + back_route
        
        files = request.files.getlist('inputExcel')
       
        prediction_choice = request.form['inputPrediction']
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           
        payload = {"filename": filename, "prediction_choice": prediction_choice}
        # submit the request
        r = ''
        while r == '':
            try:
                r = requests.post(url_back_predict, files=payload).json()
            except:
                continue  

        # ensure the request was successful
        if r["success"]:
            result = r["predictions"]
            pred = result["pred"]
            
        return render_template(return_page, pred=pred, prediction_choice=prediction_choice.capitalize())
        #return render_template(return_page, filename=filename, pred=pred, prediction_choice=prediction_choice.capitalize())


@app.route('/')
@app.route('/index')
def main():
# Delete uploaded files older than 3 hours:
    ctime = time.time()
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        mtime = os.path.getmtime(app.config['UPLOAD_FOLDER'] + file)
        if ( (ctime-mtime) > 3600*3 ):
            os.remove(app.config['UPLOAD_FOLDER'] + file)
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')


@app.route('/upload_smiles')
def upload():
    path_to_action =  '/predict_smiles'
    return render_template('upload_smiles.html', path_to_action=path_to_action)


@app.route('/predict_smiles', methods=["POST"])
def predict_smiles():
    return predict('make_prediction_smiles', 'predict_smiles.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



if __name__ == "__main__":

    app.run(host = front_server_url, port = int(port))
