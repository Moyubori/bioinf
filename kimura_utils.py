import math

symbols = 'A' 'C' 'G' 'T'


def get_matrix_for_time(time: int, _alpha: float, _beta: float):
    et = math.exp(-4 * _beta * time)
    st = (1 - et) / 4
    ut = (1 + et - 2 * math.exp(-2 * (_alpha + _beta) * time)) / 4
    rt = 1 - 2 * st - ut
    return [
        [rt, st, ut, st],
        [st, rt, st, ut],
        [ut, st, rt, st],
        [st, ut, st, rt]
    ]


def get_probability_for_transition(transition: tuple, matrix):
    # transition: (0: [ACGT] - symbol początkowy, 1: [ACGT] - symbol końcowy)
    return matrix[symbols.index(transition[0])][symbols.index(transition[1])]


def sequence_to_string(sequence: list):
    return ''.join(map(lambda element: symbols[element], sequence))
