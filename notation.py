def go():
    string = input('Ввод ')

    def converting(string):
        stack0 = list()
        stack1 = list()
        num = list()
        operators = {'+': 1, '-': 2, '*': 3, '/': 4}
        operators1 = {'+': 1, '-': 2, '*': 3, '/': 4, '(': 0}
        for i in range(0, len(string)):
            if (string[i].isdigit()) or (string[i] == '.'):
                num.append(string[i])
            elif string[i] in operators:
                stack0.append("".join(map(str, num)))
                list(num)
                num.clear()

                if stack1:
                    if (operators.get(string[i])) > (operators1.get(stack1[-1])):
                        stack1.append(string[i])
                    elif int(operators.get(string[i])) <= int(operators.get(stack1[-1])):
                        stack0.append(stack1.pop())
                        stack1.append(string[i])
                else:
                    stack1.append(string[i])
            elif string[i] == '(':
                if num:
                    stack0.append("".join(map(str, num)))
                    list(num)
                    num.clear()
                    stack1.append(string[i])
                else:
                    stack1.append(string[i])
            elif string[i] == ')':
                stack0.append("".join(map(str, num)))
                list(num)
                num.clear()
                k = 0
                stack1.reverse()
                while k == 0:
                    if stack1[k] == '(':
                        k += 1
                    else:
                        stack0.append(stack1.pop(k))
                stack1.pop(0)
                stack1.reverse()
        stack0.append("".join(map(str, num)))
        list(num)
        num.clear()
        while stack1:
            stack0.append(stack1.pop())
        k = 0
        return stack0

    def counting(stack2):
        numbers = list()
        operators = {'+': 1, '-': 2, '*': 3, '/': 4}
        k = 0
        for i in range(0, len(stack2)):
            if (stack2[i] not in operators) and (stack2[i] != ''):
                numbers.append(float(stack2[i]))
                k += 1
            elif stack2[i] == '+':
                if k > 2:
                    a = sum(numbers)
                    numbers.clear()
                    numbers.append(a)
                else:
                    op1 = numbers.pop()
                    op2 = numbers.pop()
                    a = op1 + op2
                    numbers.append(a)
                k = 0
            elif stack2[i] == '-':
                if k > 2:
                    a = numbers[0] - sum(numbers[1:])
                    numbers.clear()
                    numbers.append(a)
                else:
                    op1 = numbers.pop()
                    op2 = numbers.pop()
                    a = op2 - op1
                    numbers.append(a)
                k = 0
            elif stack2[i] == '*':
                if k > 2:
                    for i2 in range(1, len(numbers)):
                        a = numbers[0]
                        a *= numbers[i2]
                    numbers.clear()
                    numbers.append(a)
                else:
                    op1 = numbers.pop()
                    op2 = numbers.pop()
                    a = op1 * op2
                numbers.append(a)
                k = 0
            elif stack2[i] == '/':
                if k > 2:
                    for l in range(1, len(numbers)):
                        a = numbers[0]
                        a /= numbers[l]
                    numbers.clear()
                    numbers.append(a)
                else:
                    op1 = numbers.pop()
                    op2 = numbers.pop()
                    a = op2 / op1
                    numbers.append(a)
                k = 0
        a = numbers.pop()
        return a

    print(string + '=' + str(counting(converting(string))))


if __name__ == '__main__':
    go()
