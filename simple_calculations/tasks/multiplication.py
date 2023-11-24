"""
The task is to create simple and complex multiplication functions. Simple multiplication is just
multiplication of 2 numbers. Complex one -- result of multiplication of 2 or more numbers. We
assume that multiplication of 1 number is meaningless.

function1
    *   Arguments:

        * arg1
        * arg2

    *   Result:

        arg1 * arg2

function2
    *   Arguments:

        * arg1
        ...

        * arg_n (n \u2265 2)

    *   Result:

        arg1 * ... * arg_n
"""


def primitive_mult(arg1: int | float, arg2: int | float) -> int | float:
    return arg1 * arg2


def advanced_mult(*args) -> int | float:
    result = 1
    print(len(args))
    if len(args) < 2:
        raise ValueError
    for arg in args:
        result *= arg
    if int(result) == result:
        result = int(result)
    return result


if __name__ == "__main__":
    print(advanced_mult(5, -6, 7.7))
