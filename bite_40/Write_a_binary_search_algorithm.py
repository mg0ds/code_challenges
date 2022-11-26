import math

def binary_search(sequence, target):
    L = 0
    R = len(sequence) - 1
    while L <= R:
        m = math.floor((L + R)/2)
        if sequence[m] < target:
            L = m + 1
        elif sequence[m] > target:
            R = m - 1
        else:
            return m
    return None
