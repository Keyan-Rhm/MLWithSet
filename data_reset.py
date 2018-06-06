import os
import shutil

dataDir = "Dataset/"
setTrainDir = "Set_Card_Game/train/Set/"
setValDir = "Set_Card_Game/val/Set/"
notSetTrainDir = "Set_Card_Game/train/notSet/"
notSetValDir = "Set_Card_Game/val/notSet/"

raw_input("Press Enter to reset files...")

files = os.listdir(setTrainDir)

if ".DS_Store" in files: files.remove(".DS_Store")

for f in files:
    shutil.move(setTrainDir + f, dataDir)

files = os.listdir(setValDir)

if ".DS_Store" in files: files.remove(".DS_Store")

for f in files:
    shutil.move(setValDir + f, dataDir)

files = os.listdir(notSetTrainDir)

if ".DS_Store" in files: files.remove(".DS_Store")

for f in files:
    shutil.move(notSetTrainDir + f, dataDir)

files = os.listdir(notSetValDir)

if ".DS_Store" in files: files.remove(".DS_Store")

for f in files:
    shutil.move(notSetValDir + f, dataDir)