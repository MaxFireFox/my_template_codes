"""
Let's create 3 classes (Student, Teacher,
Homework) and their interactions.
1. Homework accepts 2 attributes: task text and number of days remaining until the deadline.
When it's created, the exact day and time are saved.
Attributes:
    text - string containing task text
    deadline - datetime.timedelta type object containing the number of days remaining
    created - exact date and time when this class instance was created
Methods:
    is_active - checks, whether the homework is expired or not,
    returns boolean (True if not expired)
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - accepts Homework type object and, if homework
    is expired, prints 'You are late' and returns nothing, else returns Homework
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - accepts task text and number of days, returns Homework instance
There would be others variables, attributes and methods necessary for creating the
interaction between classes above -- we'll try to name them according to PEP8
"""
from datetime import *


def printer(text):
    print(text)


class Homework:
    """
        Homework class
    """

    def __init__(self, text, deadline):
        """
        Homework has two parameters: task text and time left to do it. Also, creation time of class instance is saved.

        :param text: string containing homework name, task to do, required data, etc.
        :param deadline: datetime.timedelta object indicating time left for homework to be finished
        """
        self.text = text
        self.deadline = deadline
        self.created = datetime.now()

    def is_active(self):
        """
        Checks if homework is still not overdue

        :return: False if homework is overdue and True otherwise
        """
        return datetime.now() - self.created < self.deadline


class Student:
    def __init__(self, last_name, first_name):
        """
        Creates student class instance with these surname and name

        :param last_name: person's surname
        :param first_name: person's name
        """
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework):
        """
        Function for student to do homework if there's still time before deadline

        :param homework: task for student to do
        :return: homework if it's not overdue and
        None with stdout message "You are late" otherwise
        """
        if homework.is_active():
            return homework
        return printer("You are late")


class Teacher:
    def __init__(self, last_name, first_name):
        """
        Creates teacher class instance with these surname and name

        :param last_name: person's surname
        :param first_name: person's name
        """
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, days):
        """
        Creates homework class instance with topic/task objectives/etc and days left to do it

        :param text: string containing homework name, task to do, required data, etc.
        :param days: datetime.timedelta object indicating amount of days left until deadline
        :return: homework class instance
        """
        return Homework(text, timedelta(days))


if __name__ == '__main__':
    teacher = Teacher('Shadrin', 'Daniil')
    student = Student('Petrov', 'Roman')
    print(teacher.last_name)  # 'Shadrin'
    print(student.first_name)  # 'Roman'

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2023-11-26 14:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late