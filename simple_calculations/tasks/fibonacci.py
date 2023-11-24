"""
We'll assert whether a given number is part if fibonacci sequence. First function asserts, whether number is
part of original sequence starting with 1 and 1. Second one asserts whether it belongs to a generalization of
the Fibonacci sequence starting with given numbers. We assume that starting numbers are integer.

original:
    Argument:

        * number

    Result:

    True/False (whether number belongs to the sequence or not)

generalized:
    Arguments:

        * start1

        * start2

        * number

    Result:

    True/False (whether number belongs to the sequence or not)
"""


def fibonacci_og(number: int, start=[1, 1]) -> bool:
    seq = start.copy()
    i = 0
    while seq[1 - i] < number:
        seq[i] = seq[i] + seq[1 - i]
        i = 1 - i
    return seq[1 - i] == number


def fibonacci_gen(start1: int, start2: int, number: int) -> bool:
    seq = [start1, start2]
    i = 0
    while seq[i] * seq[1 - i] <= 0:
        if seq[i] == number:
            return True
        seq[i] = seq[i] + seq[1 - i]
        i = 1 - i
    if seq[i] * number < 0:
        return False
    if seq[i] == number:
        return True
    return fibonacci_og(abs(number), [abs(seq[i]), abs(seq[1 - i])])
# In order to save the space, we overwrite list of two numbers, not saving every single element of sequence.


if __name__ == "__main__":
    print(fibonacci_og(3))
    print(fibonacci_gen(80, -51, -8))
