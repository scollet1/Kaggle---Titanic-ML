# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/18 15:52:47 by scollet           #+#    #+#              #
#    Updated: 2017/11/18 15:52:49 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from keras.layers import Activation, Dense
from keras.models import Sequential
from keras.optimizers import Adam
import numpy as np
import keras

class Network():
    def __init__(self, inputs, outputs):
        self.input_size = inputs
        self.output_size = outputs
        self.model = self._build_model()
    def _build_model(self):
        keras.initializers.Constant(value=0)
        model = Sequential()
        model.add(Dense(128, input_dim=self.input_size, activation='sigmoid'))
        model.add(Dense(64, activation='sigmoid'))
        model.add(Dense(32, activation='sigmoid'))
        model.add(Dense(self.output_size, activation='sigmoid'))
        model.compile(loss='mean_squared_error', optimizer='Adam', metrics=['accuracy'])
        return model
    def fit(self, inputs, target, valid_inputs, valid_target):
        self.model.fit(
        inputs,
        target,
		validation_data=(valid_inputs, valid_target),
		epochs=1,
		batch_size=64,
		verbose=1)
    def predict(self, X):
        return self.model.predict(X)
    def load(self, name):
        self.model.load_weights(name)
    def save(self, name):
        self.model.save_weights(name)
