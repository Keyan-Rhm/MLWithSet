import shutil
import random
import glob
import os

setFileName = "Set"
notSetFileName = "notSet"

test_directory = "Data_Testing"
train_directory = "Data_Training"
validate_directory = "Data_Validation"

set_directory = "Dataset/Set_Dataset"
notSet_directory = "Dataset/notSet_Dataset"

sets = glob.glob(set_directory + "/*")
notSets = glob.glob(notSet_directory + "/*")
random.shuffle(notSets)

for index, set in enumerate(sets):
	if(index % 10) == 1:
		shutil.copyfile(sets[index], os.path.join(test_directory, setFileName) + "/" + os.path.basename(sets[index]) + ".jpg")
		shutil.copyfile(notSets[index], os.path.join(test_directory, notSetFileName) + "/" + os.path.basename(notSets[index]) + ".jpg")

	elif(index % 10) == 2:
		shutil.copyfile(sets[index], os.path.join(validate_directory, setFileName) + "/" + os.path.basename(sets[index]) + ".jpg")
		shutil.copyfile(notSets[index], os.path.join(validate_directory, notSetFileName) + "/" + os.path.basename(notSets[index]) + ".jpg")

	else:
		shutil.copyfile(sets[index], os.path.join(train_directory, setFileName) + "/" + os.path.basename(sets[index]) + ".jpg")
		shutil.copyfile(notSets[index], os.path.join(train_directory, notSetFileName) + "/" + os.path.basename(notSets[index]) + ".jpg")

