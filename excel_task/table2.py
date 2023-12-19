import matplotlib.pyplot as plt
from openpyxl import load_workbook
from datetime import datetime

wb = load_workbook('data.xlsx')
sheet = wb['Лист1']


def months_pos():
    i = 2
    months = {}
    while sheet['C' + str(i)].value:
        if sheet['C' + str(i)].value not in ['ОПЛАЧЕНО', 'ПРОСРОЧЕНО', 'НА ПОДПИСАНИИ', 'В РАБОТЕ', 'ВНУТРЕННИЙ']:
            months[sheet['C' + str(i)].value] = i
        i += 1
    return months


def question1(pos):
    i = pos['Июль 2021'] + 1
    july_sum = 0
    while sheet['B' + str(i)].value:
        if sheet['C' + str(i)].value == 'ОПЛАЧЕНО':
            july_sum += sheet['B' + str(i)].value
        i += 1
    return round(july_sum, 2)


def question2():
    """
    При условии, что мы рассматриваем как выручку за месяц все средства из столбца sum под указанным месяцем
    вплоть до следующего
    :return: график выручки
    """
    i = 2
    months = []
    sum_months = []
    while sheet['C' + str(i)].value:
        if sheet['C' + str(i)].value not in ['ОПЛАЧЕНО', 'ПРОСРОЧЕНО', 'НА ПОДПИСАНИИ', 'В РАБОТЕ', 'ВНУТРЕННИЙ']:
            months.append(sheet['C' + str(i)].value)
            sum_months.append(0)
        else:
            sum_months[-1] += sheet['B' + str(i)].value
        i += 1
    x = [i for i in range(len(months))]
    plt.plot(x, sum_months)
    plt.title("Вопрос №2", fontsize=25, color="black")
    plt.xticks(x, labels=months)
    plt.yticks(sum_months, labels=[str(round(i, 2)) for i in sum_months])
    plt.show()


def question3(pos):
    """
        При условии, что мы рассматриваем как выручку за месяц все средства из столбца sum под указанным месяцем
        вплоть до следующего
        :return: лучший менеджер по итогу месяца
    """
    managers = {}
    i = pos['Сентябрь 2021'] + 1
    while sheet['D' + str(i)].value:
        if sheet['D' + str(i)].value in managers:
            managers[sheet['D' + str(i)].value] += sheet['B' + str(i)].value
        else:
            managers[sheet['D' + str(i)].value] = sheet['B' + str(i)].value
        i += 1
    max_income = 0
    MVP = "(K)NoW_NAME"
    for manager in managers:
        if managers[manager] > max_income:
            max_income = round(managers[manager], 2)
            MVP = manager
    return MVP


def question4(pos):
    cnt = \
        {
            'текущая': 0,
            'новая': 0
        }
    i = pos['Октябрь 2021'] + 1
    while sheet['E' + str(i)].value:
        cnt[sheet['E' + str(i)].value] += 1
        i += 1
    if cnt['текущая'] > cnt['новая']:
        return 'текущая'
    return 'новая'


def question5(pos):
    i = pos['Май 2021'] + 1
    cnt = 0
    while sheet['A' + str(i)].value:
        x = sheet['H' + str(i)].value
        # если требуется только наличие даты получения оригинала
        if type(x) is datetime and x.month == 6:
        # если также требуется наличие слова оригинал в столбце document
        # if sheet['G' + str(i)].value == 'оригинал' and sheet['H' + str(i)].value.month == 6:
            cnt += 1
        i += 1
    return cnt


def calc_income(row):
    # если требуется только наличие даты получения оригинала
    if type(sheet['H' + str(row)].value) is datetime:
    # если также требуется наличие слова оригинал в столбце document
    # if sheet['G' + str(row)].value == 'оригинал':
        price = sheet['B' + str(row)].value
        nc = sheet['E' + str(row)].value
        status = sheet['C' + str(row)].value
        if nc == 'новая' and status == 'ОПЛАЧЕНО':
            return round(0.07*price, 2)
        elif nc == 'текущая' and status != 'ПРОСРОЧЕНО':
            return round(0.05 * price, 2) if price > 10000 else round(0.03 * price, 2)
    return 0


def task(pos):
    i = 3
    managers = {}
    while i < pos['Июль 2021']:
        sale = sheet['D' + str(i)].value
        date = sheet['H' + str(i)].value
        """В случае,если считаются только невыплаченные остатки:"""
        if type(date) is datetime and date > datetime(2021, 7, 1):
            if sale in managers:
                managers[sale] += calc_income(i)
            else:
                managers[sale] = calc_income(i)
        i += 1
    return managers


if __name__ == '__main__':
    positions = months_pos()
    print("Вопрос №1 ", question1(positions))
    question2()
    print("Вопрос №3 ", question3(positions))
    print("Вопрос №4 ", question4(positions))
    print("Вопрос №5 ", question5(positions))
    managers = task(positions)
    for manager in managers:
        print(f"У менеджера {manager} на момент 01.07.2021 остаток составил {round(managers[manager], 2)}")
