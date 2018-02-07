from itertools import product
from itertools import permutations
from itertools import combinations
from random import sample

a = ["g", "p", "r"]
b = ["d", "s", "o"]
c = ["0", "1", "2"]
d = ["1", "2", "3"]

e = list(product(a, b, c, d))
print len(e)

allTriples = list(permutations(e,3))
print(len(allTriples))
print allTriples[0]


sets = filter(
    lambda _: all(
        [
            # look at all unique values of each property and see if there is 1 or 3
            len(set([a[i] for a in _])) in {1,3} for i in range(4)
        ]
    )
    ,
    allTriples
)
print len(sets)
print sets[0]


nonSets = list(set(allTriples) - set(sets))
print len(nonSets)
print nonSets[0]

setImages = []
nonSetImages = []

for item in sets:
	setImages.append(('Set_Dataset_Renamed_1/' + item[0][0] + item[0][1] + item[0][2] + item[0][3] + '.png',
					 'Set_Dataset_Renamed_1/' + item[1][0] + item[1][1] + item[1][2] + item[1][3]  + '.png',
					 'Set_Dataset_Renamed_1/' + item[2][0] + item[2][1] + item[2][2] + item[2][3]  + '.png'))

for item in nonSets:
	nonSetImages.append(('Set_Dataset_Renamed_1/' + item[0][0] + item[0][1] + item[0][2] + item[0][3] + '.png',
					 'Set_Dataset_Renamed_1/' + item[1][0] + item[1][1] + item[1][2] + item[1][3]  + '.png',
					 'Set_Dataset_Renamed_1/' + item[2][0] + item[2][1] + item[2][2] + item[2][3]  + '.png'))

import sys
from PIL import Image
import os

dataDirectory = "Dataset"
setDirectory = "Set_Dataset"
notSetDirectory = "notSet_Dataset"

if not os.path.exists(dataDirectory):
    os.makedirs(dataDirectory)

if not os.path.exists(os.path.join(dataDirectory, setDirectory)):
    os.makedirs(os.path.join(dataDirectory, setDirectory))

finalSetDirectory = os.path.join(dataDirectory, setDirectory)

if not os.path.exists(os.path.join(dataDirectory, notSetDirectory)):
    os.makedirs(os.path.join(dataDirectory, notSetDirectory))

finalNotSetDirectory = os.path.join(dataDirectory, notSetDirectory)

for index, images in  enumerate(setImages):
	imageSet = map(Image.open, [images[0], images[1], images[2]])
	widths, heights = zip(*(i.size for i in imageSet))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in imageSet:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	new_im.save(os.path.join(finalSetDirectory, 'set' + str(index + 1) + '_' + os.path.splitext(os.path.basename(images[0]))[0] + os.path.splitext(os.path.basename(images[1]))[0] + os.path.splitext(os.path.basename(images[2]))[0] + '.png'))

for index, images in enumerate(nonSetImages):
	imageSet = map(Image.open, [images[0], images[1], images[2]])
	widths, heights = zip(*(i.size for i in imageSet))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in imageSet:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	new_im.save(os.path.join(finalNotSetDirectory, 'notSet' + str(index + 1) + '_' + os.path.splitext(os.path.basename(images[0]))[0] + os.path.splitext(os.path.basename(images[1]))[0] + os.path.splitext(os.path.basename(images[2]))[0] + '.png'))


