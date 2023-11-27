import pytest
from unittest.mock import patch
import classes.tasks.school as school
from datetime import *
import time


@pytest.mark.parametrize(
    ["text", "deadline", "wait", "expected_result"],
    [
        ("Blitzkrieg", timedelta(0, 10), 11, "You are late"),
        ("Successful Blitzkrieg", timedelta(0, 10), 9.9, school.Homework),
    ],
)
def test_hw(text: str, deadline: timedelta, wait: int, expected_result):
    hw = school.Homework(text, deadline)
    time.sleep(wait)
    with patch("classes.tasks.school.printer") as perm_mock:
        perm_mock.return_value = "You are late"
        actual_result = school.Student.do_homework(hw)
        if isinstance(actual_result, str):
            assert actual_result == expected_result
        else:
            assert isinstance(actual_result, expected_result)


@pytest.mark.parametrize(
    ["teacher_last_name", "teacher_first_name", "student_last_name", "student_first_name", "days", "expected_result"],
    [
        ("Werner", "Hans", "Miller", "Helga", 11, school.Homework),
        ("\n", "\t", "Ll$#", "\u0c2b", 0, "You are late"),
    ],
)
def test_teacher_student(teacher_last_name: str, teacher_first_name: str, student_last_name: str,
                         student_first_name: str, days: int, expected_result):
    teacher = school.Teacher(teacher_last_name, teacher_first_name)
    student = school.Student(student_last_name, student_first_name)
    homework = teacher.create_homework("text - blablabla", days)
    with patch("classes.tasks.school.printer") as perm_mock:
        perm_mock.return_value = "You are late"
        actual_result = student.do_homework(homework)
        if isinstance(actual_result, str):
            assert actual_result == expected_result
        else:
            assert isinstance(actual_result, expected_result) and \
                   actual_result.deadline == timedelta(days=days)
