import numpy as np
import random
import os
import shutil

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

numTraining = 2000
numValidation = 500

dataDir = "Dataset/"
setTrainDir = "Set_Card_Game/train/Set/"
setValDir = "Set_Card_Game/val/Set/"
notSetTrainDir = "Set_Card_Game/train/notSet/"
notSetValDir = "Set_Card_Game/val/notSet/"

if allAtOnce:
	for setCards in os.listdir(dataDir):
		
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
	for setCards in  os.listdir(dataDir):
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

random.shuffle(sets)
random.shuffle(notSets)

for item in sets[:numTraining]: 
	shutil.move(dataDir + item, setTrainDir)
	sets.remove(item)

for item in sets[:numValidation]: 
	shutil.move(dataDir + item, setValDir)
	sets.remove(item)

for item in notSets[:numTraining]: 
	shutil.move(dataDir + item, notSetTrainDir)
	notSets.remove(item)

for item in notSets[:numValidation]: 
	shutil.move(dataDir + item, notSetValDir)
	notSets.remove(item)

execfile("Resnet_Retraining.py")

execfile("data_reset.py")






