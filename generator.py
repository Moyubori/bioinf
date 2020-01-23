import sys
import random
import math

symbols = 'A' 'C' 'G' 'T'

alpha = 1 / 4
beta = 1 / 4

transitionMatrix = [
    [(1 - 2 * beta - alpha), beta, alpha, beta],  # A
    [beta, (1 - 2 * beta - alpha), beta, alpha],  # C
    [alpha, beta, (1 - 2 * beta - alpha), beta],  # G
    [beta, alpha, beta, (1 - 2 * beta - alpha)],  # T
]


def sequence_to_string(sequence: list):
    return ''.join(map(lambda element: symbols[element], sequence))


def matrix_to_string(matrix: list):
    return ''.join(map(lambda element: str(element) + ' ', sum(matrix, [])))


sequenceLength = int(sys.argv[1])
evolutionTime = int(sys.argv[2])

initialDNA = []

for i in range(0, sequenceLength):
    initialDNA.append(random.randint(0, len(symbols) - 1))

print('Initial sequence: ' + sequence_to_string(initialDNA))

firstSequence = initialDNA.copy()
secondSequence = initialDNA.copy()

for t in range(0, evolutionTime):
    st = (1-exp(-4*beta*t))/4
    ut = (1+exp(-4*beta*t)-2*exp(-2*(alpha+beta)*t))/4
    rt = 1-2*st-ut;
    transitionMatrixAfterT = [
        [rt,st,ut,st],
        [st,rt,st,ut],
        [ut,st,rt,st],
        [st,ut,st,rt]
    ]
    for sequence in (firstSequence, secondSequence):
        for index in range(0, len(sequence)):
            rand = random.random()
            for i in range(0, 4):
                probability = transitionMatrixAfterT[sequence[index]][i]
                if rand < probability:
                    sequence[index] = i
                    break
                rand = rand - probability

mappedSequences = (sequence_to_string(firstSequence), '\n', sequence_to_string(secondSequence))
print('Evolved sequence #1: ' + mappedSequences[0])
print('Evolved sequence #2: ' + mappedSequences[2])
file = open('sequences.txt', 'w')
file.writelines(mappedSequences)
file.close()

file = open('matrix.txt', 'w')
file.write(matrix_to_string(transitionMatrix))
file.close()
