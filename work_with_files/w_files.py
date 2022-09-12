""" Работа с файлами """

# Операции над файлами:
# 1. Чтение
# 2. Запись

# Файлы бывают текстовыми и бинарными

# open(путь_до_файла, режим работы) - фунцкия для открытие файлов

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

"""
r - режим чтения
w - режим записи, создает файл, перезаписывает содержимое этого файла,
если такой файл существует
x - запись если файла не сущетсвует, иначе исключение 
a - дозаписи
w+, r+ - запись и чтение 
b - открытие бинарных файлов 
t - открытие текстовых файлов
rt - режим по умолчанию 
"""


# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# read(n) - читает весь файл или n символов, если указан 

# file1 = open('test.txt')
# for row in file1:
#     print(row)
# file1.close()

# file2 = open('test.txt')
# words = file2.readlines()
# list_ = []
# for word in words:
#     list_.append(word.strip())
# print(list_)
# file2.close()

# readlines() - читает файл и возвращает список из строк

# image = open('kartinka.jpg', 'rb')
# print(len(image.read()))
# image.close()

# file5 = open('test2.txt')
# print(file5.read())
# file5.seek(0)
# print(file5.read())
# print(file5.tell())
# file5.close()

# seek(n) - перенос курсора на n позицию
# tell() - сообщает положение курсора

# with open('test2.txt', 'r') as file10:
#     a = 10
#     print(file10.read())

# print(a)

# with функция() as название: - контекстный менеджер
#     тело менеджера

# try:
#     file10.read()
# finally:
#     file10.close()

# with open('test2.txt', 'r') as file1:
#     print(file1.readlines())

# file1.read()

""" Режим записи """

# with open('test3.txt', 'w') as f:
#     f.write('apple\n')
#     f.write('banana\n')
#     f.write('pear\n')
#     f.write('tomato\n')

# with open('test4.txt', 'w+') as f:
#     list_ = ['invoker', 'sf', 'slark', 'void']
#     n = [name + '\n' for name in list_]
#     f.writelines(n)
#     f.seek(0)
#     print(f.read())

# with open('prog.txt', 'w+') as f:
#     f.write('for i in range(1, 10):\n\tprint(i)')
#     f.seek(0)
#     code = f.read()
#     exec(code)

