import sys

symbols = 'A' 'C' 'G' 'T'

sequencesFilename = sys.argv[1]
matrixFilename = sys.argv[2]

sequences = []
matrix = []

sequencesFile = open(sequencesFilename, 'r')
lines = sequencesFile.readlines()
sequencesFile.close()
for line in lines:
    sequences.append(map(lambda symbol: symbols.index(symbol), line))

matrixFile = open(matrixFilename, 'r')
line = matrixFile.readline()
matrixFile.close()
index = 0
tempArray = []
for element in line.split():
    if index == 4:
        index = 0
        matrix.append(tempArray)
        tempArray = []
    tempArray.append(str(element))
    index = index + 1

