def convert(num: int, to_type: str) -> str:
    TYPES = {
        'bin': 'Двоичная - {:b}',
        'oct': 'Восьмиричная - {:o}',
        'hex': 'Шестнадцатиричная - {:x}'
        }
    NUMBERS_NAMES = {
      0: 'Ноль',
      1: 'Один',
      2: 'Два',
      3: 'Три',
      4: 'Четыре',
      5: 'Пять',
      6: 'Шесть',
      7: 'Семь',
      8: 'Восемь',
      9: 'Девять'
    }
    if to_type and to_type in TYPES.keys():
        return f'{NUMBERS_NAMES[num]}\n{TYPES[to_type].format(num)}'
    else:
        return f'{NUMBERS_NAMES[num]}'


print(convert(num=2, to_type='bin'))
print(convert(num=3, to_type=''))
print(convert(num=9, to_type='oct'))
