import pytest
from list_sort.tasks.merge_sort import merge_sort


@pytest.mark.parametrize(
    ["lst"],
    [
        ([5, 8, 7, 9, 0, 3, 5, -9],),
        ([8, 800, 5, 5, 5, 3, 5, 3, 5],),
        ([5, 8, 7, 8, 9, 8, 7, 6, 5, 4, 8, 3, 2, 1],)
    ],
)
def test_hw(lst):
    new_lst = merge_sort(lst)
    is_sorted = True
    for i in range(len(new_lst) - 1):
        if new_lst[i] > new_lst[i + 1]:
            is_sorted = False
    assert is_sorted
