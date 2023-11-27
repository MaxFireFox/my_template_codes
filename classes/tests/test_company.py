import pytest
from classes.tasks.company import *


@pytest.mark.parametrize(
    ["companies", "dept_heads", "depts"],
    [
        (
            [
                "Coke",
                "Pepsi",
                "Dr.Pepper"
            ],
            [
                {
                    "Marketing": "Kotik Bobbie",
                    "Production": "Ivanov Ivan",
                },
                {
                    "Production": "Semyonov Aleksey",
                    "Q&A": "Novikov Nikolay"
                },
                {}
            ],
            [
                {
                    "Marketing":
                        [
                            "Drake Nataniel",
                            "Wake Alan",
                            "Yang Welt"
                        ],
                    "Production":
                        [
                            "Nokianvirtanen Joachim",
                            "Bazhenov Evgeniy"
                        ]
                },
                {
                    "Production":
                        [
                            "Kenway Connor",
                            "Kenway Edward"
                        ],
                    "Q&A":
                        [
                            "Kenway Haytham"
                        ]
                },
                {
                    "R&D":
                        [
                            "Antonov Dmitriy",
                            "Krugov Valentin"
                        ]
                }
            ]
        ),
    ],
)
def test_hw(companies, dept_heads, depts):
    i = 0
    companies_list = []
    for company in companies:
        new_company = Company(company)
        [Dept_Head(*dept_heads[i][dept].split(" "), new_company, dept) for dept in dept_heads[i]]
        for dept in depts[i]:
            [Employee(*employee.split(" "), new_company, dept) for employee in depts[i][dept]]
        if i == 1:
            # print(companies_list[0])
            # print(new_company)
            traitor = companies_list[0].department["Marketing"][1]
            new_company.employ(traitor, "Q&A")
            companies_list += [new_company]
            # for comp in companies_list:
            #     print(comp)
        else:
            companies_list += [new_company]
            # if i > 1:
            #     print(new_company)
        i += 1
    assert traitor in companies_list[1].department["Q&A"]
    assert traitor not in companies_list[0].department["Marketing"]
