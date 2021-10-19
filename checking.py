calc = input('Введите строку ')
def Checking(string):
    i = 0
    check = 0
    syntax = False
    while i != len(string):
        if string[i] == '(':
            check = check + 1
            i = i+1
        elif string[i] == ')':
            check = check - 1
            i = i + 1
            if check < 0:
                syntax = False
                break

    if check != 0:
        syntax = False
    elif check == 0:
        syntax = True

    if syntax == True:
        print('Syntax correct')
    else:
        print('Syntax error')


    return syntax

Checking(calc)


