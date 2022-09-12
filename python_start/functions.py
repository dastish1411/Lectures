""" Функции """

# print()
# max()
# pow()

# Функция - именнованный блок кода, который принимает какие-либо значения,
# совершает над ними определенные действия и возвращает результат этих действий. 

# a1 = 100
# (a1 ** 2) / 10 * 15
# a2 = 200
# (a1 ** 2) / 10 * 15
# a3 = 400
# (a1 ** 2) / 10 * 15

# DRY(Don't repeat yourself) - не повторяйся 

# def func():
#     print('hello world')

# func()

# def my_sqr(num):
#     print((num ** 2) / 10 * 15)

# a = my_sqr(100) # None
# a + 500 # TypeError

# def my_func(num):
#     return (num ** 2) / 10 * 15

# b = my_func(100) # 15000.0
# print(b)
# print(b + 500)

# a = print()
# print(a)

# def func():
#     return None

# def имя_функции(параметры):
#     тело_функции

# return - ключевое слово для возвращения результата выполнения функции

# имя_функции(аргументы)

# параметры - это значения функции при обьявлении

# аргументы - это значения для функции при вызове

# def add(x: int, y: int) -> int:
#     """ Принимает два числа и складывает их между собой """ # строка документации(docstring)
#     num = x + y
#     return num

# print(add(40, 70))
# print(add('adasd', 'asdsadf'))


# параметры бывают 2 типов:
# 1. обязательные(с)
# 2. необязательные(по умолчанию) (с=10)

# def sub(x, y):
#     res = x - y
#     return res

# print(sub(10, 25)) 

# def sub1(x, y=5):
#     res = x - y
#     return res

# print(sub1(10))
# print(sub1(50, 10))

# def func(x=5, y): # SyntaxError

# def func(a, b, c, d, e=10, f=20):
#     pass # Ok

# pass - заглушка

# аргументы бывают:
# 1. именнованные
# 2. позиционные

""" Аргументы """

# def my_func(num1 ,num2, num3=10):
#     return num1 + num2 + num3

# позиционные 
# my_func(10, 25, 30) # 65
# my_func(50, 60) # 120

# именнованные
# my_func(num1=5, num2=10, num3=15)
# my_func(num3=10, num1=5, num2=7)
# my_func(10, 5 num3=10) # 25
# my_func(num3=5, 5, 9) # Error
# my_func(10, 5, num1=15) # Error

# def send_message(email, message):
#     return f'{message} было отправлено на {email}'

# def notify_user(name):
#     message = input('Введите сообщение ')
#     email = input('Введите почту ')
#     note = send_message(email, message)
#     print(f'Здравствуйте {name}.{note}')
 
 
# notify_user('aktan')

# *args - кортеж позиционных аргументов(arguments)
# **kwargs - словарь именнованных аргументов(keyword arguments)

# def func(*args, **kwargs):
#     print(args, 'args')
#     print(kwargs, 'kwargs')

# # func(1, 2, 3, 4,) # args -> (1, 2, 3, 4)
# # func(a=1, b=2, c=3, d=4) # kwargs -> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# func(1, 2, 3, 4,a=1, b=2, c=3, d=4)

# def my_func(*args):
#     counter = 0
#     for i in args:
#         counter += i
#     return counter

# print(my_func(1,2,3,4,'asdasdas',5)) 

''' Homework '''

# def my_func(*args):
#     counter = 0
#     for i in args:
#         try:
#             counter += i
#         except TypeError:
#             print(f'{i} не является числом!')
#     return counter

# print(my_func(1,2,3,4,'adasd',6))



# def get_count(sentence):
#     count = 0
#     for i in sentence:
#         if i in 'aeiou':
#             count +=1
#     return count


# a = 'invoker'
# print(get_count(a))

# def get_count(sentence):
#     return sum([1 for i in sentence if i in 'aeuio'])

# print(get_count('asdasdasf'))

# def open_or_senior(data):
#     res = []
#     for m in data:
#         if m[0] >= 55 and m[1] > 7:
#             res.append('Senior')
#         else:
#             res.append('Open')
#     return res
            

    

# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# print(open_or_senior(input))
                
                