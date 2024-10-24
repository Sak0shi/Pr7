print('Решаемое уравнение: x = 7*b + 2*c - a')
def Check_input(a):
    innumber = input(f'Введите число {a}: ')
    try:
        dec_number = float(innumber)
        return dec_number
    except ValueError:
        print('Ошибка. Введите корректное число: ')
        return Check_input(a)

a = Check_input('a')
b = Check_input('b')
c = Check_input('c')
X = 7*b + 2*c - a
print(f'Корень вашего уравнения: {X}')
