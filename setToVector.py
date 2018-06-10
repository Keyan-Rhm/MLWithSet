import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, Flatten, MaxPooling2D, Conv2D
from keras.callbacks import Callback

from math import ceil
import os
import shutil
import random
import glob

from PIL import Image

def binarify(x):
  index = 0
  while index < len(x):
    if (x[index] == 0 or x[index] == 1):
      x.insert(index, 0)
      index += 2
    elif (x[index] == 2):
      x[index] = 1
      x.insert(index + 1, 0)
      index += 2

def normalize(x):
  for index, val in enumerate(x):
    x[index] = val/2


class TestCallback(Callback):
  def __init__(self, test_data):
    self.test_data = test_data
    
    def on_epoch_end(self, epoch, logs={}):
      x, y = self.test_data
      loss, acc = self.model.evaluate(x, y, verbose=1)
      print('\nTesting loss: {}, Testing acc: {}\n'.format(loss, acc))

with open("dataset.txt") as textFile:
  content = textFile.readlines()
  setVectors = [map(int, y) for y in [x.strip() for x in content]]

for vector in setVectors:
  binarify(vector)
# normalize(vector)

filelist = glob.glob('Dataset/*')
setImages = np.array([np.array(Image.open(fname)) for fname in filelist[:400]])

cutoff = int(len(setImages) * 0.8)

setVectors = setVectors[:400]

x_test = setImages[:cutoff]
y_test = setVectors[:cutoff]

x_train = setImages[cutoff:]
y_train = setVectors[cutoff:]

set2vec = Sequential()

set2vec.add(Conv2D(32, (3, 3), input_shape = (100, 600, 3), activation = 'relu'))

set2vec.add(MaxPooling2D(pool_size = (2, 2)))

set2vec.add(Conv2D(64, (3, 3), input_shape = (100, 600, 3), activation = 'relu'))

set2vec.add(Conv2D(64, (3, 3), input_shape = (100, 600, 3), activation = 'relu'))

set2vec.add(MaxPooling2D(pool_size = (2, 2)))

set2vec.add(Flatten())

set2vec.add(Dense(units=512, activation='relu'))

set2vec.add(Dropout(rate=0.5))

#set2vec.add(Dense(units=12, activation='softmax'))
set2vec.add(Dense(units=24, activation='softmax'))

set2vec.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])

set2vec.fit(np.array(x_train), np.array(y_train),
          epochs=50,
          batch_size=128,
          callbacks=[TestCallback((np.array(x_test), np.array(y_test)))])

score = set2vec.evaluate(np.array(x_test), np.array(y_test), batch_size=128)



