from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.callbacks import EarlyStopping
from keras.optimizers import SGD
from keras.initializers import he_normal

import os
import glob
import shutil

import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.imagenet_utils import preprocess_input

def readImg(filename):
    img              = load_img(filename, target_size=(64, 64))  
    imgArray         = img_to_array(img)  
    imgArrayReshaped = np.expand_dims(imgArray, axis=0)
    imgProcessed     = preprocess_input(imgArrayReshaped, mode='tf')
    return img, imgProcessed

SGD = SGD(lr = 0.1, decay = 1e-6, momentum = 0.9, nesterov = False)

earlystop = EarlyStopping(monitor='val_acc', min_delta=0.01, patience=5,
                          verbose=1, mode='auto')

callbacks_list = [earlystop]


from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization

#AlexNet with batch normalization in Keras 
#input image is 224x224

setIdentifier = Sequential()

setIdentifier.add(Conv2D(96, (3, 3), strides = (4, 4), input_shape = (11, 11, 3), activation = 'relu'))

setIdentifier.add(MaxPooling2D(pool_size = (2, 2), dim_ordering="tf"))

setIdentifier.add(Conv2D(256, (3, 3), input_shape = (5, 5, 48), activation = 'relu'))

setIdentifier.add(MaxPooling2D(pool_size = (2, 2), dim_ordering="tf"))

setIdentifier.add(Conv2D(384, (3, 3), input_shape = (3, 3, 256), activation = 'relu'))

setIdentifier.add(Conv2D(384, (3, 3), input_shape = (3, 3, 192), activation = 'relu'))

setIdentifier.add(Conv2D(256, (3, 3), input_shape = (3, 3, 192), activation = 'relu'))

setIdentifier.add(Flatten())

setIdentifier.add(Dense(units=4096, activation = 'relu'))
setIdentifier.add(Dropout(rate=0.5))
setIdentifier.add(Dense(units=4096, activation = 'relu'))
setIdentifier.add(Dropout(rate=0.5))
setIdentifier.add(Dense(units = 1, activation = "sigmoid"))

setIdentifier.compile(optimizer = SGD, loss='binary_crossentropy', metrics = ['accuracy'])

# gooseIdentifier = Sequential()
# gooseIdentifier.add(Convolution2D(64, 3, 11, 11, border_mode='full'))
# gooseIdentifier.add(BatchNormalization((64,226,226)))
# gooseIdentifier.add(Activation('relu'))
# gooseIdentifier.add(MaxPooling2D(poolsize=(3, 3)))

# gooseIdentifier.add(Convolution2D(128, 64, 7, 7, border_mode='full'))
# gooseIdentifier.add(BatchNormalization((128,115,115)))
# gooseIdentifier.add(Activation('relu'))
# gooseIdentifier.add(MaxPooling2D(poolsize=(3, 3)))

# gooseIdentifier.add(Convolution2D(192, 128, 3, 3, border_mode='full'))
# gooseIdentifier.add(BatchNormalization((128,112,112)))
# gooseIdentifier.add(Activation('relu'))
# gooseIdentifier.add(MaxPooling2D(poolsize=(3, 3)))

# gooseIdentifier.add(Convolution2D(256, 192, 3, 3, border_mode='full'))
# gooseIdentifier.add(BatchNormalization((128,108,108)))
# gooseIdentifier.add(Activation('relu'))
# gooseIdentifier.add(MaxPooling2D(poolsize=(3, 3)))

# gooseIdentifier.add(Flatten())
# gooseIdentifier.add(Dense(12*12*256, 4096, init='normal'))
# gooseIdentifier.add(BatchNormalization(4096))
# gooseIdentifier.add(Activation('relu'))
# gooseIdentifier.add(Dense(4096, 4096, init='normal'))
# gooseIdentifier.add(BatchNormalization(4096))
# gooseIdentifier.add(Activation('relu'))
# gooseIdentifier.add(Dense(1, 1000, init='normal'))
# gooseIdentifier.add(BatchNormalization(1000))
# gooseIdentifier.add(Activation('sigmoid'))

# setIdentifier = Sequential()

# setIdentifier.add(Conv2D(64, (3, 3), input_shape = (64, 64, 3), activation = 'relu', kernel_initializer='random_uniform', bias_initializer=he_normal(seed=None)))

# setIdentifier.add(MaxPooling2D(pool_size = (2, 2)))

# setIdentifier.add(Conv2D(64, (3, 3), input_shape = (64, 64, 3), activation = 'relu' , kernel_initializer='random_uniform', bias_initializer=he_normal(seed=None)))

# setIdentifier.add(Conv2D(64, (3, 3), input_shape = (64, 64, 3), activation = 'relu', kernel_initializer='random_uniform', bias_initializer=he_normal(seed=None)))

# setIdentifier.add(MaxPooling2D(pool_size = (2, 2)))

# setIdentifier.add(Flatten())

# setIdentifier.add(Dense(units=512, activation = 'relu', kernel_initializer='random_uniform', bias_initializer=he_normal(seed=None)))

# setIdentifier.add(Dropout(rate=0.5))

# setIdentifier.add(Dense(units = 1, activation = "sigmoid"))

# setIdentifier.compile(optimizer = SGD, loss='binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,
                shear_range = 0.2, 
                zoom_range = 0.2, 
                horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('Data_Training', 
                                                target_size = (64, 64),
                                                batch_size = 32,
                                                class_mode = 'binary')

test_set = test_datagen.flow_from_directory('Data_Testing',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

setIdentifier.fit_generator(training_set, 
                                steps_per_epoch = 324,
                                epochs = 50, 
                                validation_data = test_set,
                                validation_steps = 40,
                                callbacks = callbacks_list)

setIdentifier.save("setIdentifier.h5")

# for filename in glob.glob('validation_set/Goose/*'):
#     img, arr = readImg(filename)
#     probability = gooseIdentifier.predict(arr)
#     if probability[0][0] == 1:
#     	shutil.move(filename, "Validation_False Negatives/" + os.path.basename(filename))
#     else:
#     	shutil.move(filename, "Validation_True Positives/" + os.path.basename(filename))

# for filename in glob.glob('validation_set/NotGoose/*'):
#     img, arr = readImg(filename)
#     probability = gooseIdentifier.predict(arr)
#     if probability[0][0] == 1:
#     	shutil.move(filename, "Validation_True Negatives/" + os.path.basename(filename))
#     else:
#     	shutil.move(filename, "Validation_False Positives/" + os.path.basename(filename))

# gooseIdentifier.save("isGoose.h5")

