first_num = (input('Введите первое число: '))
second_num = (input('Введите второе число: '))
operator = input('Введите оператор /, //, +. -, *, **, % : ')

if '.' in first_num:
    first_num = float(first_num)
else:
    first_num = int(first_num)
if '.' in second_num:
    second_num = float(second_num)
else:
    second_num = int(second_num)

if operator == '+':
    print(first_num + second_num)
elif operator == '-':
    print(first_num - second_num)
elif operator == '/':
    if second_num == 0:
        print('На ноль делить нельзя')
    else:        
        print(first_num / second_num)
elif operator == '//':
    if second_num == 0:
        print('На ноль делить нельзя')
    else:        
        print(first_num // second_num) 
elif operator == '*':
    print(first_num * second_num)
elif operator == '**':
    print(first_num ** second_num)
elif operator == '%':
     if second_num == 0:
        print('На ноль делить нельзя')
     else:        
        print(first_num % second_num) 
else:
    print('Такой операции не существует!')