from rdkit.Chem import DataStructs
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv1D, Dropout, MaxPooling1D, LSTM, Bidirectional, GRU, TimeDistributed
import PreProcessing as PP

def model():
    model = Sequential()

    model.add(Conv1D(64, kernel_size=(10), input_shape=(2048,1), activation='relu'))
    model.add(MaxPooling1D(10))
    model.add(Dropout(0.5))
    model.add(LSTM(20))
    model.add(Dense(1, activation='sigmoid'))

    model = model.compile(loss=keras.losses.binary_crossentropy,
              optimizer='adam',#keras.optimizers.SGD(lr=0.01,decay=0.001, momentum=0.9, nesterov=True),
              metrics=['accuracy'])

    return model

def training_model():
    x_train, x_val, x_test, y_train, y_val, y_test = PP.PreProcess(path_smiles)
    model = model.fit(x_train, y_train, epochs=5, batch_size=64, verbose=1, validation_data=(x_val, y_val))
    model.save('back_end/Model/servier.h5')
    return    
     
