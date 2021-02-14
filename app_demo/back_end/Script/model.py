from rdkit.Chem import DataStructs
import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, Conv1D, Dropout, MaxPooling1D, LSTM, GlobalMaxPooling1D
import PreProcessing as PP

def model():
    model = Sequential()

    model.add(Embedding(max_len, 16, input_length=max_len))
    model.add(Conv1D(32, kernel_size=(5), activation='relu'))
    model.add(MaxPooling1D(5))
    #model.add(Dropout(0.8))
    model.add(Conv1D(32, kernel_size=(5), activation='relu'))
    model.add(MaxPooling1D(5))
    
    model.add(GlobalMaxPooling1D())
    model.add(Dense(1, activation='sigmoid'))

    model = model.compile(loss=keras.losses.binary_crossentropy,
              optimizer='rmsprop',
              metrics=['accuracy'])

    return model

def training_model():
    x_train, x_val, x_test, y_train, y_val, y_test = PP.PreProcess(path_smiles)
    model = model.fit(x_train, y_train, epochs=5, batch_size=64, verbose=1, validation_data=(x_val, y_val))
    model.save('back_end/Model/servier.h5')
    return    
     
