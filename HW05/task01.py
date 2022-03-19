# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
#

class Org:
    def __init__(self, org_name, quart_profits):
        self.org_name = org_name
        self.quart_profits = self.__str_to_list__(quart_profits)
        self.profit = sum(self.quart_profits)

    def __str_to_list__(self, str_, separator=' '):
        return [float('0' + profit) for profit in str(str_).split(separator)]


class MyAnalytic:
    def __init__(self, data_orgs):
        self.data_orgs = data_orgs

    def get_profits(self):
        return [org.profit for org in self.data_orgs]

    def get_average(self):
        return sum(self.get_profits()) / len(self.data_orgs) if len(self.data_orgs) > 0 else 0

    def get_report(self):
        avg = self.get_average()
        list_gt_avg = [org for org in self.data_orgs if org.profit > avg]
        list_le_avg = set(self.data_orgs) - set(list_gt_avg)

        report = f'Средняя прибыль (за год для всех предприятий): {avg:.2f}\n' \
                 f'Организации, чья прибыль выше среднего:\n'
        for org in list_gt_avg:
            report += f'\t{org.org_name}   (прибыль {org.profit:.2f})\n'
        report += f'Остальные организации:\n'
        for org in list_le_avg:
            report += f'\t{org.org_name}   (прибыль {org.profit:.2f})\n'

        return report


def main():
    num_orgs = int(input('Укажите число организаций (0 - для демо): '))

    if num_orgs == 0:
        org1 = Org('R&C Industrials', '10_000 20_000 30_000 40_000')
        org2 = Org('Maxxima Limited', '12_000 22_000 32_000 34_000')
        org3 = Org('Lucia Group Inc', '15_000 15_000 15_000 55_000')
        org4 = Org('Economistix Ltd', '10_000 20_000 10_000 10_000')
        org5 = Org('Volque East LLC', '0 0 0 87000')
        print(MyAnalytic([org1, org2, org3, org4, org5]).get_report())
        return

    orgs_input_list = []
    for _ in range(num_orgs):
        org_name = input('Укажите наименование организации: ')
        org_profit = input('Укажите через пробел квартальные прибыли организации: ')
        orgs_input_list.append(Org(org_name, org_profit))
    print('')
    print(MyAnalytic(orgs_input_list).get_report())


if __name__ == "__main__":
    main()
