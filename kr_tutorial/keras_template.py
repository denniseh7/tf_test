#Keras Tutorial

#Imports: keras for NN
import tensorflow as tf
import keras as kr
import keras.layers as ly

#add a model/NN
model=kr.Sequential()

#add layers
model.add(ly.Dense(units=64, activation='relu', input_dim=100))
model.add(ly.Dense(units=10, activation='softmax'))

#add loss function
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

#alternative loss function if you want more customization
#model.compile(loss=kr.losses.categorical_crossentropy(), optimizer=kr.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))

#train model on all data
model.fit(x_train, y_train, epochs=5, batch_size=32)

#alternative only train on specific batch
#model.train_on_batch(x_batch, y_batch)

#evaluate model
loss_and_metrics=model.evaluate(x_test, y_test, batch_size=128)

#predict using trained model
classes=model.predict(x_test, batch_size=128)