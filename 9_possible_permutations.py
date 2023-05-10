
from itertools import permutations

def possible_permutations(elements):
    result = permutations(elements)
    for x in result:
        yield list(x)




[print(n) for n in possible_permutations([1, 2, 3])]

