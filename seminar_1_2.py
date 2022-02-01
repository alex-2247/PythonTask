











# # По д/з: Анастасия, преподаватель: (Задачи 1, 3, 5, 7, 9, 11, 13, 15) 
# # (из старого "Большого списка"), по итогам первого семинара
# #
# # Раздел: Почувствуй себя интерном*
# # Задача 1. По двум заданным числам проверять является ли первое квадратом второго
# #
# def SquareCheck(arg1, arg2):
#     if arg1 == (arg2 * arg2):
#         return f"{arg1} это квадрат числа {arg2}"
#     else: 
#         return f"{arg1} не является квадратом числа {arg2}"
# #
# # основной кодоблок задачи
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# print(SquareCheck(number1, number2))





# # Раздел: Почувствуй себя интерном*
# # Задача 3. По заданному номеру дня недели вывести его название
# def WeekDayName(argDay):
#     dayNames = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
#     if 1<=argDay<=7:
#         argDay -= 1
#         return dayNames[argDay]
#     else: return f'В неделе нет дня с номером {argDay}'
# #
# # основной кодоблок задачи
# number = int(input('Введите номер дня недели: '))
# print(WeekDayName(number))





# # Раздел: Почувствуй себя интерном*
# # Задача 5. Написать программу вычисления значения функции y = f(a)
# # функция рекомендована - Sin/Cos. Встроенный системный метод принимает 
# # аргументы в радианах, поэтому чтобы работать с человеческими единицами,
# # их надо конвертить. Но в этой задачке заниматься этим не будем.
# #
# def MyCos(arg):
#     return f'Угол = {arg} радиан, его Cos = {math.cos(arg)}'
# # основной кодоблок задачи
# import math     # без этого задача не работает
# angle = float(input('Введите угол(рад.): '))
# print(MyCos(angle))





# # Раздел: Почувствуй себя интерном*
# # Задача 7. Показать числа от -N до N
# def SeventhTask(arg):
#     retVal = ""
#     for i in range(-arg, arg+1):
#         retVal = retVal + f'{i}; '
#     return retVal
# #
# myNumber = int(input('Введите число N: '))
# print(SeventhTask(myNumber))





# # Раздел: Почувствуй себя интерном*
# # Задача 9. Показать последнюю цифру трёхзначного числа
# def FindLastDigit(arg):
#     return f'Последняя цифра числа {arg} - {arg%10}'
# # основной кодоблок задачи
# from random import randint
# myNumber = randint(100,999)
# print(FindLastDigit(myNumber))





# # Раздел: Почувствуй себя интерном*
# # Задача 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# def MaxDigit(arg):
#     dig1 = arg//10
#     dig2 = arg%10
#     if dig1 > dig2: return dig1
#     else: return dig2
# # основной кодоблок задачи
# from random import randint
# SourceVal = randint(10,99)
# print(f'В числе {SourceVal} наибольшая цифра: {MaxDigit(SourceVal)}')





# # Раздел: Почувствуй себя интерном*
# # Задача 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
# # Оба число сгенерим путём Random().Next
# def CheckMultiples(arg1, arg2):
#     reminder = arg1%arg2
#     if reminder == 0: return f'Число {arg1} кратно числу {arg2}'
#     else: return f'Число {arg1} не кратно {arg2}, остаток от деления: {reminder}'
# # основной кодоблок задачи
# from random import randint
# number = randint(10,99)
# divider = randint(1,9)
# print(CheckMultiples(number, divider))





# # Раздел: Почувствуй себя джуном*
# # 15. Дано число. Проверить кратно ли оно 7 и 23
# #
# def CheckMultiples15(num, div):
#     if num % div == 0:
#         return f"кратно {div}"
#     else:
#         return f"НЕкратно {div}"
# # основной кодоблок задачи
# from random import randint
# number = randint(7, 93)     # бОльший диапазон не нужен
# divider1 = 7
# divider2 = 23
# outputString = f'Проверяемое число {number}:  '
# outputString += f'{CheckMultiples15(number, divider1)},  '
# outputString += f'{CheckMultiples15(number, divider2)}'
# print(outputString)
