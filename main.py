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
lines = matrixFile.readlines()
matrixFile.close()
for line in lines:
    matrix.append(map(lambda element: float(element), line.split()))

