import sys
import random

symbols = 'A' 'C' 'G' 'T'

alpha = 1 / 4
beta = 1 / 4

transitionMatrix = (
    ((1 - 2 * beta - alpha), beta, alpha, beta),  # A
    (beta, (1 - 2 * beta - alpha), beta, alpha),  # C
    (alpha, beta, (1 - 2 * beta - alpha), beta),  # G
    (beta, alpha, beta, (1 - 2 * beta - alpha)),  # T
)

sequenceLength = int(sys.argv[1])
evolutionTime = int(sys.argv[2])

initialDNA = []


def sequence_to_string(sequence: list):
    return ''.join(map(lambda element: symbols[element], sequence))


for i in range(0, sequenceLength):
    initialDNA.append(random.randint(0, len(symbols) - 1))

print('Initial sequence: ' + sequence_to_string(initialDNA))

firstSequence = initialDNA.copy()
secondSequence = initialDNA.copy()

for t in range(0, evolutionTime):
    for sequence in (firstSequence, secondSequence):
        for index in range(0, len(sequence) - 1):
            rand = random.random()
            for i in range(0, 3):
                probability = transitionMatrix[sequence[index]][i]
                if rand < probability:
                    sequence[index] = i
                    break
                rand = rand - probability

print('Evolved sequence #1: ' + sequence_to_string(firstSequence))
print('Evolved sequence #2: ' + sequence_to_string(secondSequence))
