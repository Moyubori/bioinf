import sys
import random
import kimura_utils as dna

alpha = 1 / 4
beta = 1 / 4

transitionMatrix = [
    [(1 - 2 * beta - alpha), beta, alpha, beta],  # A
    [beta, (1 - 2 * beta - alpha), beta, alpha],  # C
    [alpha, beta, (1 - 2 * beta - alpha), beta],  # G
    [beta, alpha, beta, (1 - 2 * beta - alpha)],  # T
]


def matrix_to_string(matrix: list):
    return ''.join(map(lambda element: str(element) + ' ', sum(matrix, [])))


sequenceLength = int(sys.argv[1])
evolutionTime = int(sys.argv[2])

initialDNA = []

for i in range(0, sequenceLength):
    initialDNA.append(random.randint(0, len(dna.symbols) - 1))

print('Initial sequence: ' + dna.sequence_to_string(initialDNA))

firstSequence = initialDNA.copy()
secondSequence = initialDNA.copy()

for t in range(0, evolutionTime):
    for sequence in (firstSequence, secondSequence):
        for index in range(0, len(sequence)):
            rand = random.random()
            for i in range(0, 4):
                probability = transitionMatrix[sequence[index]][i]
                if rand < probability:
                    sequence[index] = i
                    break
                rand = rand - probability

mappedSequences = (dna.sequence_to_string(firstSequence), '\n', dna.sequence_to_string(secondSequence))
print('Evolved sequence #1: ' + mappedSequences[0])
print('Evolved sequence #2: ' + mappedSequences[2])
file = open('sequences.txt', 'w')
file.writelines(mappedSequences)
file.close()

file = open('matrix.txt', 'w')
file.write(str(alpha) + ' ' + str(beta))
file.close()
