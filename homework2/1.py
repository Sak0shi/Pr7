def Check_input():
    innumber = input('Введите число: ')
    try:
        dec_number = float(innumber)
        return dec_number
    except ValueError:
        print('Ошибка. Введите корректное число: ')
        return Check_input()

def binary(n):
    digs = '01'
    if n < 0:
        return '-' + binary(-n)
    elif n == 0:
        return '0'
    buf = n % 2
    return binary(n // 2) + digs[buf]

def Octanry(n):
    digs = '01234567'
    if n < 0:
        return '-' + binary(-n)
    elif n == 0:
        return '0'
    buf = n % 8
    return binary(n // 8) + digs[buf]


n = Check_input()
n1 = binary(int(n))
n2 = Octanry(int(n))

print(f'Ваше число в двоичной системе:{n1}\nВаше число в восьмеричной системе счисления:{n2}')
