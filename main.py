a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Выберите действие:\n1-сложение\n2-вычитание\n3-умножение\n4-деление')

def add(x,y):
    z = int(x) + int(y)
    print(str(x) + '+' + str(y) + '=' + str(z))
    return z
def sub(x,y):
    z = int(x) - int(y)
    print(str(x) + '-' + str(y) + '=' + str(z))
    return z
def mul(x,y):
    z = int(x) * int(y)
    print(str(x) + 'x' + str(y) + '=' + str(z))
    return z
def div(x,y):
    z = int(x) / int(y)
    print(str(x) + '/' + str(y) + '=' + str(z))
    return z
if c == '1':
    add(a,b)
elif c == '2':
    sub(a,b)
elif c == '3':
    mul(a,b)
elif c == '4':
    div(a,b)
else:
    print('Нет такого действия(')

