""" Область видимости и пространства имен """

# LEGB - пространства имен
# Local - локальная
# Enclosed - замкнутая
# Global - глобальная
# Built-in - встроенная 

# Область видимости - часть программ, где будет доступно то 
# или иное имя(переменная, функция, класс и т.д.)

# name = 'Janat'
# name = 'Akbar'

# print(name) # Akbar

# name = 'Marina' # global

# # def func():
# #     name = 'Nikolay'
# #     print(name)

# # print(name)
# # func()

# def func2():
#     # local
#     print(name)

# func2()

# def func3():
#     a = 10
#     print(a) # NameError

# Имена из локальной области недоступны в глобальной области,
# но в локальной области доступны имена из глобальной области

# for i in range(1, 10):
#     res = i * 2

# print(res)

# number = 20
# if number % 2 != 0:
#     res2 = 35

# print(res2)

# num = 10

# def func():
#     global num
#     num = 50
#     num2 = 30

# func()
# print(num)

# x = 20 
# def func_outer():
#     x = 15 # nonlocal
#     def func_inner():
#         x = 25 # local
#         print(x)
#         def inner_func():
#             x = 70
#         inner_func()
#     func_inner()

# func_outer() # 25

# number = 20 
# def outer_func():
#     # nonlocal
#     number = 19
#     print(number) # 19
#     def inner_func():
#         nonlocal number 
#         number = 25
#         print(number) # 25
#     inner_func()
#     print(number) # 25

# outer_func() # 19

""" Встроенная область """

# print()
# def
# return

""" globals(), locals() """

# a = 20
# print(globals())
# globals() - показывает имена на глобальном уровне видимости

# print(locals())
# def my_func():
#     var = 95
#     tel = 100
#     print(locals())
#     print(globals())

# my_func()

# loclas() - показывает доступные имена той области, в которой была вызвана 

# def get_grade(mark):
#     mark = 1
#     grade = 0
#     if mark > 87:
#         grade = 5
#     return grade

# print(get_grade(88))

# именнованный блок кода

# def func_name(a=100, b=200):
#     return a + b 


# print(func_name(b=400))

# def func(a, b, c):
#     return a + b + c

# nums = (3, 4, 8)
# dict_ = {'a':10, 'b': 20, 'c':40}
# print(func(*nums))
# print(func(**dict_))

# def my_func(x, y):
#     print('Before return')
#     return x + y
#     print('asdasd')

# print(my_func(10, 20))

# def my_func(x, y):
#     if x > y:
#         return x + y
#     else:
#         return x - y
    
# print(my_func(10, 20))

# a = tuple(i for i in range(1,10))
# print(a)

# def func():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# print(list(func()))

# def func(x):
#     for i in range(x):
#         yield i

# a = func(10)
# for i in a:
#     print(i)
