from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.callbacks import EarlyStopping
from keras.optimizers import SGD
from keras.utils import to_categorical
from keras.layers.advanced_activations import LeakyReLU
from keras.regularizers import l2

import os
import glob
import shutil

import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.imagenet_utils import preprocess_input

earlystop = EarlyStopping(monitor='val_acc', min_delta=0.001, patience=5,
                          verbose=1, mode='auto')

callbacks_list = [earlystop]

# opt = SGD(lr=0.01)

setIdentifier = Sequential()

setIdentifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

setIdentifier.add(MaxPooling2D(pool_size = (2, 2)))

setIdentifier.add(Conv2D(64, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

setIdentifier.add(Conv2D(64, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

setIdentifier.add(MaxPooling2D(pool_size = (2, 2)))

setIdentifier.add(Conv2D(64, (3, 3), input_shape = (128, 64, 3), activation = 'relu'))

setIdentifier.add(MaxPooling2D(pool_size = (2, 2)))

setIdentifier.add(Flatten())

setIdentifier.add(Dense(units=512, activation = 'relu'))

setIdentifier.add(Dropout(rate=0.5))

setIdentifier.add(Dense(units = 2, activation = "softmax"))

setIdentifier.compile(optimizer = "adam", loss='categorical_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory("Data_Training", 
												target_size = (64, 64),
												batch_size = 32,
												class_mode = 'categorical')

test_set = test_datagen.flow_from_directory("Data_Testing",
											target_size = (64, 64),
											batch_size = 32,
											class_mode = 'categorical')

setIdentifier.fit_generator(training_set, 
								steps_per_epoch = 486,
								epochs = 50, 
								validation_data = test_set,
								validation_steps = 60,
								callbacks = callbacks_list)

setIdentifier.save("setIdentifier.h5")


# for filename in glob.glob('Data_Validation/Set/*'):
#     img, arr = readImg(filename)
#     probability = setIdentifier.predict(arr)
#     if probability[0][0] == 1:
#         shutil.copyfile(filename, "Results/Validation_TruePos/" + os.path.basename(filename))
#     else:
#         shutil.copyfile(filename, "Results/Validation_FalseNeg/" + os.path.basename(filename))

# for filename in glob.glob('Data_Validation/notSet/*'):
#     img, arr = readImg(filename)
#     probability = setIdentifier.predict(arr)
#     if probability[0][0] == 1:
#         shutil.copyfile(filename, "Results/Validation_FalsePos/" + os.path.basename(filename))
#     else:
#         shutil.copyfile(filename, "Results/Validation_TrueNeg/" + os.path.basename(filename))


# def readImg(filename):
#     img              = load_img(filename, target_size=(64, 64))  
#     imgArray         = img_to_array(img)  
#     imgArrayReshaped = np.expand_dims(imgArray, axis=0)
#     imgProcessed     = preprocess_input(imgArrayReshaped, mode='tf')
#     return img, imgProcessed


