import pytest
from typing import List
from simple_calculations.tasks.fibonacci import fibonacci_og, fibonacci_gen


@pytest.mark.parametrize(
    ["number", "start", "expected_result"],
    [
        [3, (3, -2), (True, True)],
        [-4, (3, -4), (False, True)],
        [4, (-2, 3), (False, True)],
        [1, (-2, 3), (True, True)],
        [0, (80, -50), (False, True)],
        [8, (80, -51), (True, False)],
        [7, (80, -51), (False, True)],
        [-15, (80, -51), (False, True)],
        [-8, (80, -51), (False, True)],
    ]
)
def test_mult(number: int, start: tuple[int, int], expected_result: tuple[bool, bool]):
    assert fibonacci_og(number) == expected_result[0]
    assert fibonacci_gen(start[0], start[1], number) == expected_result[1]
