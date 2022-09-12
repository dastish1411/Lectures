""" Списки и циклы """

# list()
# Список - изменяемый, упрорядочный, индексируемый, итерируемый тип данных.
# Нужен для хранения нескольких элементов

# Элементами списка могут быть любые типы данных

# list_ = [2, 'dsa', True, False, [1, 2], None, {'a: 12'}, {1, 2},('a', 'b', 'c')]
# print(list_)

# list1 = [1, 2, 3, 4, 5, [6, 7]]
#       #  0  1  2  3  4   5
# list[0] # 1
# list[1] # 2
# list[2] # 3
# list[5] # [6, 7]
# list[5][0] # 6
# list[-1] # [6, 7]
# list1[1:-2] # [2, 3, 4]

""" Добавление элементов в список """



a = [1, 2, 3]
# a.append(element) - добавляет элемент в конц списка
# print('До ',a)
# a.append(4)
# print('После ', a)

# a.insert(index, element) - вставляет элемент на место указанного индекса
# print('До', a)
# a.insert(1, 'hello')
# print('После', a)

# a.append(element) -> a.insert(len(a), element)

# a.insert(1234, 12) # добавил в конец [1, 2, 3, 'world']

# a.extend(list2) - добавляет все элементы list2 в list1

# my_list1 = [4, 2, 6]
# my_list2 = [1, 3, 8]
# my_list1.extend(my_list2) 
# print(my_list1) # [4, 2, 6, 1, 3, 8]

# my_list1.append(my_list2) # [4, 2, 6, [1, 3, 8]]

# new_list = my_list1 + my_list2 # создает новый список 
# print(my_list1) # [4, 2, 6]
# print(new_list) # [4, 2, 6, 1, 3, 8]

""" Замена элементов """

# b= ['a', 'b', 'c', 'd']
# b[2] # 'c'
# b[2] = 'g'
# print(b) # ['a', 'b', 'g', 'd']

""" Удаление элементов """

ab = ['a', 'b', 'c', 'd']

# ab.pop([index]) - удаляет элемент по указанному индексу, но если индекс не указан 
# - удаляет последний элемент. Возвращает удаленный элемент

# ab.pop(1)
# print(ab) # ['a', 'c', 'd']

# ab.pop()
# print(ab) # ['a', 'b', 'c']

# deleted_el = ab.pop(2)
# print(deleted_el) # 'c'
# print(ab) # ['a', 'b', 'd']
# ab.append(deleted_el) # ['a', 'b', 'd', 'c']

# list3.remove(значение) - удаляет первый встретившийся элемент по указанным значением

# list3 = ['azamat', 'kolya', 'adilet', 'azamat']
# # list3.remove('azamat')
# # print(list3) # ['kolya', 'adilet', 'azamat']
# list3.remove(20) # ValueError

# ab.clear() - полностью очищает список 
# ab.clear()
# print(ab) # []

# del element
# del ab
# print(ab)

# del ab[3]
# print(ab) # ['a', 'b', 'c']

# del ab[:2]
# print(ab) # ['c', 'd']

# a1 = [1, 2, 3]
# b2 = a1

# b2.append(5)
# print(b2) # [1, 2, 3, 4]
# print(a1) # [1, 2, 3, 4]
# print(b2 is a1) # True

""" Копирование списка """

# a3 = [1, 2, 3]
# a4 = a3.copy()
# a5 = a3[:]

""" Сортировка списка """

# num_list = [4, 6, 3, 8, 5]
# num_list.sort()
# print(num_list) # [3, 4, 5, 6, 8]

# num_list.sort(reverse=True)
# print(num_list) # [8, 5, 4, 3]

# str_list = ['b', 'c', 'e', 'a', 'd', '!']
# str_list.sort()
# print(str_list) # ['!', 'a', 'b', 'c', 'd', 'e']

# name_list = ['Azamat', 'Ivan', 'Zeynep', 'Aliya']
# name_list.sort(key=len)
# print(name_list) # ['Ivan', 'Aliya', 'Azamat', 'Zeynep']

# name_list = ['Azamat', 'Ivan', 'Zeynep', 'Aliya']
# new = sorted(name_list, key=len, reverse=True)
# print(new) # ['Azamat', 'Zeynep', 'Aliya', 'Ivan']

# my_list = ['a', 'b', 'c', 'd', 'e']
# my_list.reverse()
# print(my_list) # ['e', 'd', 'c', 'b', 'a']

# new = my_list[::-1]
# print(new)


# b5 = ['a', 'b', 'c', 'a', 'a']
# print(b5.count('a')) # 3

# print(b5.index('c'))

""" Циклы """

# Цикл - многократное выполнение определенного участка кода 

iter_list = [1, 2, 3, 4, 5]
# print(iter_list[0])
# print(iter_list[1])
# print(iter_list[2])
# print(iter_list[3])
# print(iter_list[4])
# print(iter_list[5])

""" Виды цикла """
 
# 1. for
# 2. while

""" цикл for """
# for item in iter_list:
#     print(item)

# Итерация - повторение какого-либо действие

# for - цикл работает до тех пор, пока элементы в итерируемом обьекте не заканчиваются
# for элемент in итерируемый_обьект:
#    тело цикла

# mail_list = ['azamat', 'mirbek', 'baatai', 'alym']
# result = []
# for name in mail_list:
#     gmail = name + '@gmail.com'
#     result.append(gmail)
# print(result)

# int 
# str
# list
# bool
# tuple
# set
# dict
# None

# print(dir(list))

# types_list = [int , str, list, bool, None, set, dict, tuple]
# iter_objs = []
# non_iter_objs = []
# for obj in types_list:
#     if '__iter__' in dir(obj):
#         iter_objs.append(obj)
#     else:
#         non_iter_objs.append(obj)
# print('Итерируемые обьекты: ', iter_objs)
# print('Неитерируемые обьекты: ', non_iter_objs)

# range() - функция для генерации последовательности чисел
# range(start, stop, step)
# range(stop)
# print(list(range(10))) # преобразвание последовательности чисел в список из чисел

# num_list = []
# for num in range(100):
#     num_list.append(num)
# print(num_list)

# num_list = []
# for num in range(1, 101):
#     if num % 2 == 0:
#         num_list.append(num)

# print(num_list)

# num_list = []
# for num in range(0,101,2):
#     num_list.append(num)
# print(num_list)

# list_of_lists = [[1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]]
# for list1 in list_of_lists:
#     for elem in list1:
#         print(elem)    

""" цикл while """

# Бесконечный цикл

# num = 10
# while num < 11:
#     print(num)

# while True:
#     print('hello')

# while - цикл работает до тех порб пока условие истинно(True)

# Запрашивать цисло до тех пор пока сообщение не будет равно 'stop'
# msg = input('Введите сообщение или stop ')
# while msg != 'stop':
#     print(msg)
#     msg = input('Введите сообщение или stop ')

""" break """

# break - останавливает работу цикла

# while True:
#     msg = input('Введите сообщение или stop ')
#     if msg == 'stop':
#         print('цикл остановлен')
#         break
#     print(msg)

""" continue """

# Печатать сообщение до тех пор пока оно не будет равно 'bye'

# while True:
#     msg = input('Введите сообщение или stop ')
#     if msg == 'bye':
#         print('итерация пропущена')
#         continue
#     print(msg)

# for num in range(10):
#     print(num)
# else:
#     print('цикл окончен')


# for num in range(10):
#     if num == 5:
#         break
# else:
#     print('цикл окончен')

op = ["--x", 'x++', "x++"]
x = 0
for i in op:
    if i == '--x':
        x = x - 1
        print(x)
    elif i == 'x++':
        x = x + 1
        print(x)
print(x)        