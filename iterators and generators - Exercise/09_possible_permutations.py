from itertools import permutations


def possible_permutations(elements):
    for el in permutations(elements):
        yield list(el)