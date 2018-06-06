from keras.optimizers import SGD
from convnetskeras.convnets import preprocess_image_batch, convnet



im = preprocess_image_batch(['examples/' + img_name],img_size=(256,256), crop_size=(227,227), color_mode="rgb")

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model = convnet('alexnet',weights_path="weights/alexnet_weights.h5", heatmap=False)
model.compile(optimizer=sgd, loss='mse')

out = model.predict(im)

print out

best = -1
bestIndex = -1

for index, num in enumerate(out[0]):

	if (num > best):
		best = num
		bestIndex = index

print best
print bestIndex

	