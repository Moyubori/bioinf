import sys

symbols = 'A' 'C' 'G' 'T'


def _parse_sequences(unparsed_sequences: list):
    parsed_sequences = []
    for _line in unparsed_sequences:
        parsed_sequences.append(list(_line.strip()))
    return parsed_sequences


def _parse_matrix(unparsed_matrix: str):
    parsed_matrix = []
    index = 0
    temp_array = []
    for _element in unparsed_matrix.split():
        if index == 4:
            index = 0
            parsed_matrix.append(temp_array)
            temp_array = []
        temp_array.append(float(_element))
        index = index + 1
    parsed_matrix.append(temp_array)
    return parsed_matrix


def _get_transition_probability(_matrix, transition: tuple) -> float:
    return _matrix[symbols.index(transition[0])][symbols.index(transition[1])]


def _compute_mutation_time(time_range: range, _sequences, _matrix) -> int:
    probabilities = []
    for t in time_range:
        probabilities.append(_compute_probability_for_sequence(t, _sequences[0], _sequences[1], _matrix))
    return time_range[probabilities.index(max(probabilities))]


def _compute_probability_for_sequence(time_threshold: int, initial_sequence, final_sequence, _matrix) -> float:
    total_probability = 1
    saved_transition_probabilities = dict()
    for i in range(0, len(initial_sequence)):
        initial_symbol = initial_sequence[i]
        final_symbol = final_sequence[i]
        transition = (initial_symbol, final_symbol)
        if transition in saved_transition_probabilities:
            symbol_probability = saved_transition_probabilities[transition]
        else:
            symbol_probability = _compute_probability_for_symbol(1, time_threshold, transition, _matrix)
            saved_transition_probabilities[transition] = symbol_probability
        total_probability = total_probability * symbol_probability
    return total_probability


def _compute_probability_for_symbol(probability: float, steps_left: int, transition: tuple, _matrix) -> float:
    if steps_left == 0:
        if transition[0] == transition[1]:
            return probability
        return 0
    total_probability = 0
    for s in symbols:
        symbol_probability = _compute_probability_for_symbol(
            probability * _get_transition_probability(_matrix, (transition[0], s)), steps_left - 1, (s, transition[1]), _matrix)
        total_probability = total_probability + symbol_probability
    return total_probability


sequencesFilename = sys.argv[1]
matrixFilename = sys.argv[2]
startTime = sys.argv[3]
endTime = sys.argv[4]

sequencesFile = open(sequencesFilename, 'r')
lines = sequencesFile.readlines()
sequencesFile.close()
sequences = _parse_sequences(lines)

matrixFile = open(matrixFilename, 'r')
line = matrixFile.readline()
matrixFile.close()
matrix = _parse_matrix(line)

timeRange = range(int(startTime), int(endTime) + 1)
mutationTime = _compute_mutation_time(timeRange, sequences, matrix)

print('Most probable mutation time: ' + str(mutationTime))
