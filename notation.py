notation = input('Введите строку ')
stack0 = notation.split(' ')
k = 0
for i in range(0, len(stack0)):
    if stack0[i].isdigit() == True:
        k += 1
    elif stack0[i] == '+' or stack0[i] == '-' or stack0[i] == '*' or stack0[i] == '/':
        k -= 2
        if k != 0:
            check = False
            break
numbers = list()
signs = list()
i = 0
if check == False:
    for i in range(0, len(stack0)):
        if stack0[i].isdigit() == True:
            numbers.append(stack0[i])
        elif stack0[i] == '+' or stack0[i] == '-' or stack0[i] == '*' or stack0[i] == '/':
            signs.append(stack0[i])
    for i in range(0, len(signs)):
        a = int(numbers[i])
        b = int(numbers[i + 1])
        if signs[i] == '+':
            d = a + b
        elif signs[i] == '-':
            d = a - b
        elif signs[i] == '*':
            d = a * b
        elif signs[i] == '/':
            d = a - b
        numbers[i + 1] = d
    print('= ', d)
else:
    print('Syntax Error')
