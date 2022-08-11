""" Декораторы """

# Декораторы - это функция которая расширяет функционал другой функции 
# не изменяя её кодовой базы.

# Функия высшего порядка - принимает в качестве аргумента другую функцию
# или возвращает значения другой функции.

# def function2():
#     function1()
#     print('i am function2')

# def function1():
#     print('i am function1')

# function1()
# function2()

# def func():
#     print('i am func!!!')

# def func2(func):
#     func()
#     print('i am func2')
    
# func2(func=func)

# def func1():

#     def func2():
#         print('i am func2')

#     print('i am func1')
#     func2()

# func1()

# def func1():

#     def func2():
#         return 'i am func2'

#     print('i am func1')
#     return func2


# func = func1()

# print(func())


# def decorator(func):

#     def wrapper():
#         print('i running before main func')
#         func()
#         print('i runing after main func')
    
#     return wrapper

# @decorator  # - синтаксический сахар
# def main():
#     print('i am main function')

# # decorator_main = decorator(main)
# # decorator_main()

# main()

# def decorator_count(func):
    
#     def wrapper(name, last_name):
#         print('Добро пожаловать!!! ')
#         func(name, last_name)
#         print('Количество участников: 32')

#     return wrapper


# @decorator_count
# def main(name: str, last_name: str):
#     print(f'{name.capitalize()} {last_name.capitalize()}')

# main('python', 'dor')


# def decorator(func):

#     def wrapper(name):
#         print('Hello World')
#         func(name)
#         print('God bye')

#     return wrapper

# @decorator

# def main(name: str):
#     print(f'{name} !!!')

# main('Invoker')

# def bread(funcion):

#     def wrapper():
#         print('bread')
#         funcion()
#         print('bread')

#     return wrapper

# def salat(function):

#     def wrapper():
#         print('salat')
#         function()
#         print('salat')

#     return wrapper

# @bread
# @salat
# def func():
#     print('Котлета')

# func()

# from datetime import datetime 

# def time_check(func):

#     def wrapper(*args, **kwargs):
#         start_time = datetime.now() 
#         func(*args, **kwargs)
#         end_time = datetime.now()
#         print('время выполнения!!')
#         print(end_time - start_time)
#     return wrapper

# @time_check
# def generate_range(*args, **kwargs):
#     for i in range(args[0]):
#         print(pow(args[1], 23))

# generate_range(10, 23, b=32)
