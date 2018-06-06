import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, Flatten, MaxPooling2D
from keras.callbacks import Callback

from math import ceil
import os
import shutil
import random

text_file = open("dataset.txt", "r")

lines = text_file.read().split('\n')

lines = lines[:-1]

data = []


for line in lines:
	dataArray = map(int, list(line))
	data.append(dataArray)

def areSame(setString, index):
	return (setString[index] == setString[index + 4]) and (setString[index] == setString[index + 8]) 

def areDifferent(setString, index):
	return (setString[index] != setString[index + 4]) and (setString[index] != setString[index + 8])  and (setString[index + 4] != setString[index + 8])

while True:
	coloursMatch = raw_input('Can the colours in the set match? (y/n)')
	if (coloursMatch == "y" or coloursMatch == "n"):
		break;

while True:
	coloursDiffer = raw_input('Can the colours in the set all differ? (y/n)')
	if (coloursDiffer == "y" or coloursDiffer == "n"):
		break;

while True:
	numbersMatch = raw_input('Can the numbers in the set match? (y/n)')
	if (numbersMatch == "y" or numbersMatch == "n"):
		break;

while True:
	numbersDiffer = raw_input('Can the numbers in the set all differ? (y/n)')
	if (numbersDiffer == "y" or numbersDiffer == "n"):
		break;

while True:
	shadesMatch = raw_input('Can the shades in the set match? (y/n)')
	if (shadesMatch == "y" or shadesMatch == "n"):
		break;

while True:
	shadesDiffer = raw_input('Can the shades in the set all differ? (y/n)')
	if (shadesDiffer == "y" or shadesDiffer == "n"):
		break;

while True:
	shapesMatch = raw_input('Can the shapes in the set match? (y/n)')
	if (shapesMatch == "y" or shapesMatch == "n"):
		break;

while True:
	shapesDiffer = raw_input('Can the shapes in the set all differ? (y/n)')
	if (shapesDiffer == "y" or shapesDiffer == "n"):
		break;

while True:
	allAtOnce = raw_input('Do all of these have to be satisfied at once for a set? (y/n)')
	if (allAtOnce == "y" or allAtOnce == "n"):
		break;

coloursMatch = True if (coloursMatch == "y") else False
coloursDiffer = True if (coloursDiffer == "y") else False
numbersMatch = True if (numbersMatch == "y") else False
numbersDiffer = True if (numbersDiffer == "y") else False
shadesMatch = True if (shadesMatch == "y") else False
shadesDiffer = True if (shadesDiffer == "y") else False
shapesMatch = True if (shapesMatch == "y") else False
shapesDiffer = True if (shapesDiffer == "y") else False
allAtOnce = True if (allAtOnce == "y") else False

sets = []
notSets = []

colourIndex = 0
shapesIndex = 1
shadesIndex = 2
numbersIndex = 3

if allAtOnce:
	for setCards in data:

		coloursOK = False
		numbersOK = False
		shadesOK = False
		shapesOK = False

		if ((coloursMatch and areSame(setCards, colourIndex)) or (coloursDiffer and areDifferent(setCards, colourIndex))):
			coloursOK = True

		if (not coloursMatch and not coloursDiffer):
			coloursOK = True 

		if ((numbersMatch and areSame(setCards, numbersIndex)) or (numbersDiffer and areDifferent(setCards, numbersIndex))):
			numbersOK = True
			
		if (not numbersMatch and not numbersDiffer):
			numbersOK = True 

		if ((shadesMatch and areSame(setCards, shadesIndex)) or (shadesDiffer and areDifferent(setCards, shadesIndex))):
			shadesOK = True

		if (not shadesMatch and not shadesDiffer):
			shadesOK = True 

		if ((shapesMatch and areSame(setCards, shapesIndex)) or (shapesDiffer and areDifferent(setCards, shapesIndex))):
			shapesOK = True

		if (not shapesMatch and not shapesDiffer):
			shapesOK = True 

		isSet = coloursOK and numbersOK and shadesOK and shapesOK

		if (isSet):
			sets.append(setCards)
		else:
			notSets.append(setCards)

if not allAtOnce:
	for setCards in data:
		if ((coloursMatch and areSame(setCards, colourIndex)) or (coloursDiffer and areDifferent(setCards, colourIndex))):
			sets.append(setCards)
			continue

		if ((numbersMatch and areSame(setCards, numbersIndex)) or (numbersDiffer and areDifferent(setCards, numbersIndex))):
			sets.append(setCards)
			continue

		if ((shadesMatch and areSame(setCards, shadesIndex)) or (shadesDiffer and areDifferent(setCards, shadesIndex))):
			sets.append(setCards)
			continue

		if ((shapesMatch and areSame(setCards, shapesIndex)) or (shapesDiffer and areDifferent(setCards, shapesIndex))):
			sets.append(setCards)
			continue

		notSets.append(setCards)

numTraining = int(ceil(len(sets) - 0.1 * len(sets)))
numValidation = len(sets) - numTraining

random.shuffle(sets)
random.shuffle(notSets)

x_train = sets[:numTraining]
sets = sets[numTraining:]
y_train = [1] * numTraining

x_test = sets[:numValidation]
y_test = [1] * numValidation

x_train.extend(notSets[:numTraining])
notSets = notSets[numTraining:]
y_train.extend([0] * numTraining)

x_test.extend(notSets[:numValidation])
y_test.extend([0] * numValidation)

class TestCallback(Callback):
    def __init__(self, test_data):
        self.test_data = test_data

    def on_epoch_end(self, epoch, logs={}):
        x, y = self.test_data
        loss, acc = self.model.evaluate(x, y, verbose=0)
        print('\nTesting loss: {}, Testing acc: {}\n'.format(loss, acc))

model = Sequential()
model.add(Dense(64, input_dim=12, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(np.array(x_train), np.array(y_train),
          epochs=50,
          batch_size=128,
          callbacks=[TestCallback((np.array(x_test), np.array(y_test)))])
score = model.evaluate(np.array(x_test), np.array(y_test), batch_size=128)



