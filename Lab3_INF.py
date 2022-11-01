"""
Лабораторная работа №3
Михайлов Дмитрий Андреевич
Группа P3118
"""

import re


def Task60Points(number):
    eyes = [':', ';', 'X', '8', '=', '[']
    noses = ['-', '<', '-{', '<{']
    mouths = ['(', ')', 'O', '|', '\\', '/', 'P']
    print("Мой смайлик: " + ''.join([eyes[number % 6], noses[number % 4], mouths[number % 7]]))
    test_answers = []
    for i in range(5):
        test = input()
        test_answers.append(len(re.findall(r'=-{[)]', test)))
    print(' '.join([str(i) for i in test_answers]))


def AdditionalTask18Points():
    task = 'Уважаемые студенты! В эту субботу в 15:00 планируется доп. занятие на 2 часа. То есть в 17:00:01 оно уже кончится.'
    print(re.sub(r"(?:(\b\d{2}:\d{2}:\d{2}\b)+|(\b\d{2}:\d{2}\b))", 'TBD', task))


def AddiyionalTask22Points():
    for i in range(5):
        task = input("Введите почту: ")
        if re.fullmatch((r'(?: [A-Za-z0-9]+[._]?)*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})'), task):
            print(''.join(re.findall(r'@\w+.\w+', task)))
        else:
            print('Fail!')

isu = int(input())
print("Проверка основого задания на 60 баллов: ")
print(Task60Points(isu))
print(" ")
print("Проверка дополнительного задания на +18 баллов: ")
print(AdditionalTask18Points())
print(" ")
print("Проверка дополнительного задания на +22 балла: ")
print(AddiyionalTask22Points())
