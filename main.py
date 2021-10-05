a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Выберите действие:\n1-сложение\n2-вычитание\n3-умножение\n4-деление\n')

def add(x, y):
    z = int(x) + int(y)
    return z
def sub(x, y):
    z = int(x) - int(y)
    return z
def mul(x, y):
    z = int(x) * int(y)
    return z
def div(x, y):
    z = int(x) / int(y)
    return z

if c == '1':
    result = add(a, b)
    print(str(a)+'/'+str(b)+'='+str(result))
elif c == '2':
    result = sub(a, b)
    print(str(a)+'-'+str(b)+'='+str(result))
elif c == '3':
    result = mul(a, b)
    print(str(a)+'x'+str(b)+'='+str(result))
elif c == '4':
    result = div(a, b)
    print(str(a)+'/'+str(b)+'='+str(result))
else:
    print('Нет такого действия(')

