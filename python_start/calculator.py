num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
sign = input('Что делать: ')

if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2
elif sign == '*':
    result = num1 * num2
elif sign == '//':
    result = num1 // num2
elif sign == '/':
    result = num1 / num2
elif sign == '%':
    result = num1 % num2 
elif sign == '**':
    result = num1 ** num2
else:
    print("Нету данной операции") 
print(result)


