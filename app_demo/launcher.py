##### SET PATH 
import sys
import os
import time
import ctypes
import flask
import webbrowser
import subprocess as sp

# only to not have to actualize web page because of the time to load tensorflow in back end
from keras.models import load_model

dir_ = os.getcwd()
print(dir_)

#python_path = sys.path[0]
python_path = '/miniconda/bin/python'


# PATH OF FRONT SERVER
front_path = 'front_end/front_end_server.py'
front_path = os.path.join(dir_,front_path)

# PATH OF BACK SREVER
back_path = 'back_end/Script/main.py'
back_path = os.path.join(dir_,back_path)


frontProc = sp.Popen([python_path,front_path], shell = False)
print("Front Started")

backProc = sp.Popen( [python_path,back_path], shell = False)
print("Back Started")


# Open webrowser
front_server_url = "http://localhost:8891"
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open(front_server_url)
webbrowser.open(front_server_url)
