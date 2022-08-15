""" Встроенные функции """

# print()

""" Приведение к определенному типу """
# int()
# str()
# dict()
# list()
# set()
# tuple()
# bool()
# complex()
# float()

# pow()
# divmod()

""" Возвращает список атрибутов и методов """
# dir()

# type()
# id()

# a = 10
# print(isinstance(a, int)) # проверяет типы данных

# len()
# min()
# max()
# sum()
 
"""
map, filter, enumerate, zip, reduce

lambda 
"""

""" map() """

# map(func, iterable) - принимает функцию и какой- то итерируемый обьект.
# Применяет переданную функцию к каждому элементу итер. обьекта.

# def func1(num):
#     return num + 10

# nums = [1, 2, 3 ,4, 5]
# res = list(map(func1, nums))
# res2 = [num + 10 for num in nums]
# print(res)
# print(res2)


# def func1(list1, list2):
#     return list1 + list2
    
# nums = [1, 2, 3 ,4, 5]
# nums2 = [1, 2, 3, 4, 5, 6]
# res = list(map(func1, nums, nums2))
# print(res)

# words = ['apple', 'map', 'laptop']
# def func2(word):
#     return word + '15'

# res = map(lambda word: word + '15', words)

# res2 = map(func2, words)
# print(list(res))
# print(list(res2))

# lambda param: тело функции 
# labmda - анонимная функция, которая живет только на момент ее выполнения 

""" filter() """
# filter(func, iterable) - принимает функцию(-> bool) и итер объект.
# Фильтрует по условию указанному в функции

# nums = [75, 89, 35, 65, 43]
# def filter_num(num):
#     return num % 5 == 0

# res = filter(filter_num, nums)
# print(list(res))

# res2 = list(filter(lambda num: num % 5 == 0, nums))
# print(res2)

# res3 = [num for num in nums if num % 5 == 0]
# print(res3)

""" reduce() """

# from functools import reduce

# reduce(func, iterable) - принимает функцию, итер объект.
# Сводит все элементы итер объекта в одно значение 

# nums = [10, 20, 30, 40]
# def func3(num1, num2):
#     return num1 + num2

# res = reduce(func3, nums)
# print(res)
# print(sum(nums))

# res2 = reduce(lambda num1, num2: num1 + num2 , nums)
# print(res2)

# nums = [10, 20, 30, 40]
# min_value = reduce(lambda x, y: x if x < y else y, nums)
# x = 10, y = 20 -> x = 10, y = 30 -> x = 10, y = 40
# print(min_value)
# print(min(nums))

""" enumerate() """

# enumerate() - принимает последовательность элементов, и 
# нумерует каждый элемент последовательности

# a = 'word'
# res = enumerate(a)
# # print(list(res)) 
# print(dict(res)) 

# b = ['h', 'e', 'l', 'l', 'o']
# res2 = enumerate(b, start=12)
# # print(tuple(res2))
# for i in res2:
#     print(i)

# a = 'world'
# b = iter(a)
# while True:
#     try:
#         print(b.__next__())
#     except:
#         break

""" zip """

# zip() - связывает элементы переданных последовательностей 

# list1 = [1, 2, 3, 4, 5] 
# list2 = ['a', 'b', 'c']
# list3 = ['Masha', 'Dasha', 'Pasha']
# zipped_list = zip(list1, list2, list3)
# lista, listb, listc = zipped_list
# print(lista)
# print(listb)
# print(listc)
# print(list(zipped_list))
