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
# str8 = 'asdasd'
# print(str8.strip(symbol)) # убирает указанной символ в строке с двух сторон,
# если не указан символ, по умолчанию - пробел 
# str8.lstrip() - # - убирает пробелы слева 
# str8.rstrip() - # - убирает пробелы справа

""" Методы проверки """

string = 'My test string 123'
# print(string.isdigit()) # False - проверяет на цифры 
# print(string.isalpha()) # False - проверяет на буквы
# print(string.isalnum()) # False - проверяет на буквы и цифры
# print(string.isspace()) # False - проверяет на пробелы
# print(string.islower())  
# print(string.isupper())
# print(string.isendswith('123'))
# print(string.startswith('My'))
# print(string.islower())
# print(string.islower())

# str1 = 'apple'
# str2 = 'hello'
# print(str1 > str2)
# ord('a') # 97
# chr(97) # 'a'
# # ASCII 

# a = 'abcde'
# b = 'abced'
# print(sorted(a))
# print(sorted(b))

""" Форматирование/интерполяция строк """
# stat = 'Привет, Фархад! Приглашаю тебя на праздник!'

# name = input()
# # %
# # str5 = 'Привет, %s!' % name
# # print(str5)
# # str6 = 'Привет, {}'.format(name)
# # print(str6)
# place = input()
# str7 = f'Hello {name}! Welcome to {place}'
# print(str7)

# Форматирование строк - подстановка переменных в строку, создание динамической строки

""" Экранирование """

# a = 'I\'m student'
# b = 'Идет бычок качается,\n\tВздыхает на ходу'
# print(b)
# \n - newline
# \t - tabular

# str8 = r'This is test string\n\t\n'
# print(str8)
# # raw

# windows_path = r'Users\Documents\\new_folder'
# print(windows_path) 

# string = 'Hello world'
# string2 = 'ell'
# print(string2 in string) # True - проверяет наличие 

""" Помощник для метода """

# dir(object)
# str1 = 'hello'
# print(dir(str1)) # dir - принимает обьект и показывает все его методы

hashtags = '#makers#bootcamp#программирование#it#курсы'

result = hashtags.split('#')[1:]

print(result)