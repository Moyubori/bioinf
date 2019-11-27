import sys

symbols = 'A' 'C' 'G' 'T'


def parse_sequences(unparsed_sequences: list):
    parsed_sequences = []
    for line in unparsed_sequences:
        parsed_sequences.append(map(lambda symbol: symbols.index(symbol), line))
    return parsed_sequences


def parse_matrix(unparsed_matrix: str):
    parsed_matrix = []
    index = 0
    temp_array = []
    for element in line.split():
        if index == 4:
            index = 0
            parsed_matrix.append(temp_array)
            temp_array = []
        temp_array.append(str(element))
        index = index + 1
    return parsed_matrix


def compute_probability_for_time(time: int):
    # todo
    pass


def compute_mutation_time(time_range: range):
    probabilities = []
    for t in time_range:
        probabilities.append(compute_probability_for_time(t))
    return time_range[probabilities.index(max(probabilities))]


sequencesFilename = sys.argv[1]
matrixFilename = sys.argv[2]
startTime = sys.argv[3]
endTime = sys.argv[4]

sequencesFile = open(sequencesFilename, 'r')
lines = sequencesFile.readlines()
sequencesFile.close()
sequences = parse_sequences(lines)

matrixFile = open(matrixFilename, 'r')
line = matrixFile.readline()
matrixFile.close()
matrix = parse_matrix(line)

timeRange = range(startTime, endTime)
mutationTime = compute_mutation_time(timeRange)

print(mutationTime)
