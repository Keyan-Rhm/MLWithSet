import os

text_file = open("dataset.txt", "w")

for filename in os.listdir("Dataset"):

	vector = []
	for index, item in enumerate(filename[:12]): 
		if (filename[index] == 'g'):
			vector.append('0')
		elif (filename[index] == 'p'):
			vector.append('1')
		elif (filename[index] == 'r'):
			vector.append('2')
		elif (filename[index] == 'd'):
			vector.append('0')
		elif (filename[index] == 'o'):
			vector.append('1')
		elif (filename[index] == 's'):
			vector.append('2')
		elif ((index + 1) % 4 != 0): 
			vector.append(filename[index])
		else: 
			vector.append(str(int(filename[index]) - 1))

	vector.append('\n')
	stringForm = ''.join(vector)

	text_file.write(stringForm)

text_file.close()
