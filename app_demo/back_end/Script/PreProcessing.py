from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from feature_extractor import *
from rdkit.Chem import DataStructs


def PreProcess(path_smiles):
    
    df = pd.read_csv(path_smiles)
    df.set_index('mol_id', inplace=True)
    df['smiles'] = df['smiles'].apply(lambda x: fingerprint_features(x))
    
    X = df['smiles']
    y = df['P1']
    
    #Pas efficace
    arr = np.zeros((0,), dtype=np.int8)
    for j,i in enumerate(X):
        DataStructs.ConvertToNumpyArray(X.iloc[j], arr)
        X.iloc[j] = arr
        
    x_train, x_val, y_train, y_val = train_test_split(X,y,train_size=.6, stratify=y, shuffle=True)
    x_val, x_test, y_val, y_test = train_test_split(x_val, y_val, stratify=y_val, test_size=0.1, shuffle=True)
    
    x_train = np.stack(x_train)
    x_train = x_train.reshape((x_train.shape[0],2048,1))
    
    x_val = np.stack(x_val)
    x_val = x_val.reshape((x_val.shape[0],2048,1))

    x_test = np.stack(x_test)
    x_test = x_test.reshape((x_test.shape[0],2048,1))
    
    y_train = np.array(y_train)
    y_val = np.array(y_val)
    y_test = np.array(y_test)
    
    y_train = y_train.reshape(y_train.shape[0],1)
    y_val = y_val.reshape(y_val.shape[0],1)
    y_test = y_test.reshape(y_test.shape[0],1)
    
    return x_train, x_val, x_test, y_train, y_val, y_test


    
