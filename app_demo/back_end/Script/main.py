import os
import io
import sys
import glob
from flask import Flask, request, render_template, jsonify
from keras.models import load_model
import pandas as pd
import numpy as np
from feature_extractor import *
from rdkit.Chem import DataStructs
from keras import backend as K
import tensorflow as tf
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model



back_server_url = "localhost"

port = '8892'

app = Flask(__name__)


dir_ = os.getcwd()

UPLOAD_FOLDER = 'back_end/Data_input'
UPLOAD_FOLDER = os.path.join(dir_,UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


files=glob.glob(UPLOAD_FOLDER+"/*.*")
for f in files:
    os.remove(f)
   
path_smiles = 'smiles.csv'
path_smiles = os.path.join(UPLOAD_FOLDER,path_smiles)



def loading_model():

    model_servier_path = 'back_end/Model/servier.h5'
    model_servier_path = os.path.join(dir_,model_servier_path)
    global model
    '''
    session = tf.Session(graph=tf.Graph())
    with session.graph.as_default():
        K.set_session(session)
        model = K.models.load_model(model_servier_path)
    '''

    # load the pre-trained model
    #global graph
    #graph = tf.get_default_graph()
    model = load_model(model_servier_path)

    print('Finished loading deep models')



def model_choice(prediction_choix):

    if prediction_choix == 'Prediction':
        return model

    return model


'''
@app.route('/make_prediction_smiles', methods=["POST"])
def make_prediction_smiles(model, path_smiles):
    print('in make prediction')
    result = {"success": False}
    print('result : ',result)
    if request.method == "POST":
        
        #if request.files.get("filename"):
            #filename = request.files['filename'].read()
            #filename = filename.decode()
        
        print('before pred')
        pred = model.prediction_smiles(model, path_smiles)
                   
    result["predictions"] = {'pred': pred}
    result["success"] = True

    print(result)

    return jsonify(result)
'''
@app.route('/make_prediction_smiles', methods=["POST"])
def make_prediction_smiles():
    result = {"success": False}
    if request.method == "POST":
        smiles_prediction = pd.read_csv(path_smiles, sep=',', header=0)
        arr = np.zeros((0,), dtype=np.float16)
        smiles_prediction['smiles'] = smiles_prediction['smiles'].apply(lambda x: fingerprint_features(x))
        DataStructs.ConvertToNumpyArray(smiles_prediction.iloc[0]['smiles'], arr)
        smiles_prediction.iloc[0]['smiles'] = arr
        arr = np.stack(arr)
        arr = arr.reshape(1,2048,1)
        #with graph.as_default():
            #K.set_session(session)
        pred = model.predict_classes(arr)
        pred = float(pred)
    
    result["predictions"] = {'pred': pred}
    result["success"] = True

    print(result)

    return jsonify(result)

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
            "please wait until server has fully started"))
    loading_model()
    app.run(host = back_server_url, port = int(port))
