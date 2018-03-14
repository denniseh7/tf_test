#Dennis Hsu
#Tutorial Classification: MLP, MultiClass, SoftMax
#Level: Basic
#03/14/18

#imports: keras, numpy

#keras: high level API for deep learning, backend is tensorflow
#import all parts of MLP
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

#numpy for dataset layout
import numpy as np

#generate random data for testing
#training
#samples (1000), features(20), classes(10)
x_train=np.random.random((1000,20)) #1000 rows(samples), 20 columns (features)

# 1000 rows (samples), 1 column (label), 10 classes
y_train=keras.utils.to_categorical(np.random.randint(10, size=(1000,1)), num_classes=10)

#testing: same as training but with 100 samples instead
x_test=np.random.random((100,20))
y_test=keras.utils.to_categorical(np.random.randint(10, size=(100,1)), num_classes=10)


#Create Sequential MLP
#Input layer(20), 2 Hidden Layers(64) with DropOut, 1 OutputLayer(10)
model=Sequential()

#Hidden Layer(HL) 1 from Input Layer(IL) with Dropout(DO) Half of Neurons
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))

#HL 2 from HL 1
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

#Output Layer(OL) from HL2 with SoftMax
model.add(Dense(10, activation='softmax'))


#Optimizer for BackProp in MLP
#SGD with momentum 0.9 used in most State of the Art (SOTA) NN
#Nesterov can be used or not; has shown performance improvement so that SGD does not update too
#   much in one jump based on gradient
sgd=SGD(lr=0.01, momentum=0.9, nesterov=True)

#Put the parts of the MLP together
#loss function used to calculate error/loss: categorical cross entropy
#   use regular cross entropy for binary classification
#optimizer: SGD
#Use accuracy as measurement as output
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=['accuracy'])






