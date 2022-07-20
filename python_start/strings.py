""" Строки (strings) """

# str()

# Строки - неизменяемый, упорядоченный индексируемый тип данных

string = 'Hello'

string2 = 'Hello'

doc_string = """ Обычно используется для написания документации 
к коду"""
doc_string2 = ''' Обычно используется для написания документации в несколько строк '''

string3 = "Hello, I'm student"

string4 = 'Hello, I\'m teacher'

# str1 = 'Hello'
# str2 = 'World'
# print(str1 + str2)
# Конкатенация _ склеивание строк/сложение строк

# str3 = 'Quak '
# num1 = 3
# print(str3 * num1)

""" Функции и методы строк """

my_str = 'Hello world'

# print(len(my_str))  # - выводит длину строки
# print(my_str.split(separator)) # - делит по указанному делителю 
# (по умолчанию - пробел)

my_str.replace('l','b') # hebbo worbd - замена подстроки в строке 
my_str.upper() # HELLO WORLD - перевод в верхний регистр
my_str.lower() # hello world - перевод в нижный регистр 
my_str.title() # Hello World - перевод первого символа каждого слова в верхний регистр
my_str.capitalize() # Hello world - перевод первого символа строки в верхний регистр
my_str.casefold() # ss - эсцет - более агрессивный перевод в нижный регистр
my_str.count('l') # 3 - считает количество вхождений переданной подстроки 

""" Индексы и срезы """
# Индекс - порядковвый номер символа в строке(начиная с 0) 

# 'makers'
#  012345
# -054321   
# print(str7[-1])

str7 = 'hello world'

# print(str7[0:5])
# str7[start:stop]

# print(str7[4:]) # от старта до конца строки 
# print(str7[:7]) # от начала до указанного индекса
# print(str7[0:-1:2]) # str7 [stat:stop:step]
# print(str7[::-1]) # отрицательный шаг начинает чтение строки с конца 
str7 = 'hello world'
# print(str7.find('ell')) # 1 - поиск индекса подстроки в строке
# print(asdasdasd) # дальше будет работать 
# print(str7.index('w')) # 

# print('*'.join(['hello','world','bye'])) # hello*world*bye -
# соединяет переданный список строк по указанной строке  
str8 = 'asdasd'
# print(str8.strip(symbol)) # убирает указанной символ в строке с двух сторон,
# если не указан символ, по умолчанию - пробел 
str8.lstrip() - # - убирает пробелы слева 
str8.rstrip() - # - убирает пробелы справа

print(str8.isalpha()) # 