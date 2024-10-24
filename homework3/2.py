def Check_input():
    innumber = input('Введите число: ')
    try:
        dec_number = float(innumber)
        return dec_number
    except ValueError:
        print('Ошибка. Введите корректное число: ')
        return Check_input()

def number_to_13(n):
    digs = '0123456789ABC'
    if n<0:
        return '-' + number_to_13(-n)
    elif n == 0:
        return '0'
    buf = n % 13
    return number_to_13(n//13) + digs[buf]

N = Check_input()

N13 = number_to_13(int(N))

print('Ваше число в тринадцатеричной системе: ', N13)
