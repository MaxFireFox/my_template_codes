from typing import List


class Company:
    def __init__(self, name: str, employees=[]):
        self.name = name
        self.employees = employees
        self.department = {}
        self.dept_heads = {}

    def create_dept(self, dept: str):
        self.dept_heads[dept] = None
        self.department[dept] = []

    def employ(self, employee, dept: str):
        self.employees += [employee]
        if dept not in self.department:
            self.create_dept(dept)
        self.department[dept] += [employee]
        employee.get_hired(self, dept)

    def assign_head(self, employee, dept: str):
        self.dept_heads[dept] = employee

    def fire(self, employee, dept: str):
        # print(employee)
        # print(self)
        self.employees.remove(employee)
        if employee is Dept_Head:
            self.dept_heads[dept] = None
        self.department[dept].remove(employee)

    def __str__(self):
        info = "\nCompany_name: " + self.name + "\nDepartments:\n\n"
        for dept in self.department:
            if self.dept_heads[dept] is not None:
                info += dept + "\nDepartment Head: " + self.dept_heads[dept].get_full_name() + "\nAll employees:\n"
            else:
                info += dept + "\nNo Department Head\nAll employees:\n"
            for employee in self.department[dept]:
                if employee != self.dept_heads[dept]:
                    info += employee.get_full_name() + "\n"
            info += "\n"
        return info


class Employee:
    def __init__(self, last_name: str, first_name: str, company: Company = None, department: str = None):
        """
        Creates Employee class instance with these surname and name

        :param last_name: person's surname
        :param first_name: person's name
        :param company: Company instance that hires this person
        :param department: name of department, where this person is assigned to
        """
        self.last_name = last_name
        self.first_name = first_name
        self.company = company
        self.department = department
        if department is not None:
            company.employ(self, department)

    def get_full_name(self):
        return self.last_name + " " + self.first_name

    def get_hired(self, company: Company, department: str):
        """
        If employee is unemployed, he can get job in certain department of a company.
        If he is employed, we assume he is transferred. Using None for company and
        department can be used for dismissal

        :param company: Company instance. We assume, that one person can work only in one company
        :param department: Department instance. We assume, that one person can work only in one.
        :return: None
        """
        if self.company is None:
            self.company = company
        elif self.company != company:
            self.company.fire(self, self.department)
            self.company = company
        self.department = department

    def get_raised(self):
        """
        :return: Dept_Head instance with all the same attributes
        """
        if self.company.dept_heads[self.department] is not None:
            self.company.dept_heads[self.department].get_demoted()
        self.company.fire(self, self.department)
        new_role = Dept_Head(self.last_name, self.first_name, self.company, self.department)
        self.company.assign_head(new_role, new_role.department)
        del self
        return new_role

    def __str__(self):
        return "Usual employee of " + self.department + " department " + self.last_name + " " + self.first_name

    def __del__(self):
        if self in self.company.employees:
            self.company.fire(self, self.department)


class Dept_Head(Employee):
    def __init__(self, last_name: str, first_name: str, company: Company, department: str):
        """
        Creates Employee class instance with these surname and name

        :param last_name: person's surname
        :param first_name: person's name
        :param company: Company instance where this person is working
        :param department: name of department, where this person is assigned to
        """
        self.last_name = last_name
        self.first_name = first_name
        self.company = company
        self.department = department
        company.employ(self, department)
        company.assign_head(self, department)

    def get_demoted(self):
        """
        :return: Employee instance with all the same attributes
        """
        self.company.fire(self, self.department)
        new_role = Employee(self.last_name, self.first_name, self.company, self.department)
        del self
        return new_role

    def __str__(self):
        return "Head of " + self.department + " department " + self.last_name + " " + self.first_name


if __name__ == "__main__":
    fabric = Company("Wonka")
    fabric.create_dept("Marketing")
    Will = Employee("Turner", "Will", fabric, "Marketing")
    Faust = Dept_Head("Oligyeri", "Dante", fabric, "Marketing")
    Will = Will.get_raised()
    print(fabric)
