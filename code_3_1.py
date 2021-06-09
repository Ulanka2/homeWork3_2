class MyCustomDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month * 30
        self.year = year * 360
        self.all_day = self.day + self.month + self.year
        self.name = f'{day}.{month}.{year}'

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if self.all_day == other.all_day:
            return f'Даты {self.name} и {other.name} равны'
        else:
            return False

    def __ne__(self, other):
        if self.all_day != other.all_day:
            return f'Даты {self.name} и {other.name} не равны'
        else:
            return False

    def __lt__(self, other):
        if self.all_day < other.all_day:
            return f'Дата {self.name} меньше даты {other.name}'
        else:
            return False

    def __gt__(self, other):
        if self.all_day > other.all_day:
            return f'Дата {self.name} больше даты {other.name}'
        else:
            return False

    def __le__(self, other):
        if self.all_day <= other.all_day:
            return f'Дата {self.name} меньше даты {other.name} или равна'
        else:
            return False

    def __ge__(self, other):
        if self.all_day >= other.all_day:
            return f'Дата {self.name} больше даты {other.name} или равна'
        else:
            return False

    def __add__(self, other):
        return (f'Сумма двух дат {self.name} и {other.name} в днях равна: '
                f'{self.all_day + other.all_day}')

    def __sub__(self, other):
        diff = self.all_day - other.all_day
        if diff < 0:
            return (f'Разница двух дат {self.name} и '
                    f'{other.name} по дням: {-diff}')
        else:
            return (f'Разница двух дат {self.name} и '
                    f'{other.name} по дням: {diff}')


custom_date_1 = MyCustomDate(12, 2, 2021)
custom_date_2 = MyCustomDate(30, 5, 2009)
custom_date_3 = MyCustomDate(12, 2, 2021)
custom_date_4 = MyCustomDate(5, 12, 1874)
custom_date_5 = MyCustomDate(26, 9, 1934)

print(f'{custom_date_1}\n'
      f'{custom_date_2}\n'
      f'{custom_date_3}\n'
      f'{custom_date_4}\n'
      f'{custom_date_5}')

print(f'{custom_date_1 == custom_date_3}\n'
      f'{custom_date_2 == custom_date_5}')

print(f'{custom_date_4 != custom_date_3}\n'
      f'{custom_date_3 != custom_date_1}')

print(f'{custom_date_4 < custom_date_1}\n'
      f'{custom_date_1 < custom_date_4}')

print(f'{custom_date_1 > custom_date_4}\n'
      f'{custom_date_3 > custom_date_3}')

print(f'{custom_date_4 <= custom_date_4}\n'
      f'{custom_date_5 <= custom_date_2}\n'
      f'{custom_date_1 <= custom_date_4}')

print(f'{custom_date_1 >= custom_date_4}\n'
      f'{custom_date_3 >= custom_date_3}\n'
      f'{custom_date_5 >= custom_date_1}')

print(f'{custom_date_1 + custom_date_2}\n'
      f'{custom_date_4 + custom_date_3}')

print(f'{custom_date_1 - custom_date_2}\n'
      f'{custom_date_4 - custom_date_3}')