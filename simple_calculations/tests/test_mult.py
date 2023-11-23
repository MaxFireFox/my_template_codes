import pytest
from typing import List
from simple_calculations.tasks.multiplication import primitive_mult, advanced_mult


@pytest.mark.parametrize(
    ["input_values", "expected_result"],
    [
        [[5, 9], (45, 45)],
        [[3, 7, -8], (21, -168)],
        [[0], (ValueError, ValueError)],
        [[5, -6, 7.7], (-30, -231)],
        [[5, -6, -7.7], (-30, 231.0)],
        [[4, 2.1, 8.0], (8.4, 67.2)]
    ]
)
def test_mult(input_values: List[int | float], expected_result: tuple[int | float| Exception, int | float | Exception]):
    if len(input_values) < 2:
        try:
            result2 = advanced_mult(input_values)
            assert result2 == expected_result[1]
        except expected_result[1]:
            assert True
    else:
        result1 = primitive_mult(*input_values[:2])
        result2 = advanced_mult(*input_values)
        assert (result1, result2) == expected_result


"""
another option could be:
    try:
        result1 = primitive_mult(*input_values[:2])
        result2 = advanced_mult(*input_values)
        assert (result1, result2) == expected_result
    except ValueError:
        try:
            result2 = advanced_mult(input_values)
            assert result2 == expected_result[1]
        except expected_result[1]:
            assert True
but try/except blocks burden the system more than if/else
"""
