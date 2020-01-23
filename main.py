import sys
import kimura_utils as dna

cachedResults = dict()


def _parse_sequences(unparsed_sequences: list):
    parsed_sequences = []
    for _line in unparsed_sequences:
        parsed_sequences.append(list(_line.strip()))
    return parsed_sequences


def _parse_matrix(unparsed_matrix: str):
    return tuple(map(lambda element: float(element), unparsed_matrix.split()))


def _get_transition_probability(_matrix, transition: tuple) -> float:
    return _matrix[dna.symbols.index(transition[0])][dna.symbols.index(transition[1])]


def _compute_mutation_time(time_range: range, _sequences, _alpha, _beta) -> int:
    probabilities = []
    print('Probabilities:')
    for t in time_range:
        probability = _compute_probability_for_sequence(t, _sequences[0], _sequences[1], _alpha, _beta)
        print('t=' + str(t) + ', p=' + str(probability))
        probabilities.append(probability)
    return time_range[probabilities.index(max(probabilities))]


def _compute_probability_for_sequence(time: int, initial_sequence, final_sequence, _alpha, _beta) -> float:
    total_probability = 1
    computed_matrix = dna.get_matrix_for_time(time, _alpha, _beta)
    for i in range(0, len(initial_sequence)):
        transition_probability = dna.get_probability_for_transition(
            (initial_sequence[i], final_sequence[i]),
            computed_matrix
        )
        total_probability = total_probability * transition_probability
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
alpha, beta = _parse_matrix(line)

timeRange = range(int(startTime), int(endTime) + 1)
mutationTime = _compute_mutation_time(timeRange, sequences, alpha, beta)

print('Most probable mutation time: ' + str(mutationTime))
