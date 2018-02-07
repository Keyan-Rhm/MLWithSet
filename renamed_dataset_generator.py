import os
import shutil

directory = "Set_Dataset_1"

renamedDirectory = "Set_Dataset_Renamed_1"

if not os.path.exists(renamedDirectory):
    os.makedirs(renamedDirectory)

for filename in os.listdir(directory):
	if filename.endswith(".png"):

		renameColours =  filename.replace('green', 'g').replace('red', 'r').replace('purple', 'p')
		renameShapes = renameColours.replace('diamond', 'd').replace('oval', 'o').replace('squiggle', 's')
		renameShading = renameShapes.replace('empty', '0').replace('shaded', '1').replace('filled', '2')

		newName = renameShading
		print(newName)

		shutil.copy(os.path.join(directory, filename), os.path.join(renamedDirectory, newName)) 

