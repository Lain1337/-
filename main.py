a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Выберите действие:1-сложение, 2-вычитание, 3-умножение 4-деление ')

if c == '1':
    d = int(a) + int(b)
    print(str(a) +'+' + str(b) + '=' + str(d) )
elif c == '2':
    d = int(a) - int(b)
    print(str(a) + '-' + str(b) + '='+str(d) )
elif c == '3':
    d = int(a) * int(b)
    print(str(a) + 'x' + str(b) + '='+str(d) )
elif c == '4':
    d = int(a) / int(b)
    print(str(a) + '/' + str(b) + '='+str(d) )
else:
    print('Нет такого действия(')

