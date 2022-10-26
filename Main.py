def esc(code): #Функция для удобного объявления цветов
    return f'\u001b[{code}m'

BLACK = esc(40)
RED = esc(41)
GREEN = esc(42)
YELLOW = esc(43)
BLUE = esc(44)
MAGENTA = esc(45)
CYAN = esc(46)
WHITE = esc(47)
END = esc(0)

def flag_sw(): #Функия для пострения флага Швейцарии
    print(RED + '  ' * 5 + END)
    print(RED + '  ' * 2 + WHITE + '  ' * 1 + RED + '  ' * 2 + END)
    print(RED + '  ' * 1 + WHITE + '  ' * 3 + RED + '  ' * 1 + END)
    print(RED + '  ' * 2 + WHITE + '  ' * 1 + RED + '  ' * 2 + END)
    print(RED + '  ' * 5 + END)

def uzor_j(i): #Функция для повторяющегося узора
    print((WHITE + '  ' * 2 + BLACK + '  ' * 5 + WHITE + '  ' * 2) * i + END)
    print((WHITE + '  ' * 1 + BLACK + '  ' * 2 + WHITE + '  ' * 3 + BLACK + '  ' * 2 + WHITE + '  ' * 1) * i + END)
    print((BLACK + '  ' * 2 + WHITE + '  ' * 5 + BLACK + '  ' * 2) * i + END)
    print((BLACK + '  ' * 1 + WHITE + '  ' * 7 + BLACK + '  ' * 1) * i + END)
    print((BLACK + '  ' * 1 + WHITE + '  ' * 7 + BLACK + '  ' * 1) * i + END)
    print((BLACK + '  ' * 1 + WHITE + '  ' * 7 + BLACK + '  ' * 1) * i + END)
    print((BLACK + '  ' * 2 + WHITE + '  ' * 5 + BLACK + '  ' * 2) * i + END)
    print((WHITE + '  ' * 1 + BLACK + '  ' * 2 + WHITE + '  ' * 3 + BLACK + '  ' * 2 + WHITE + '  ' * 1) * i + END)
    print((WHITE + '  ' * 2 + BLACK + '  ' * 5 + WHITE + '  ' * 2) * i + END)

#Вывод в консоль задания 1 и 2

flag_sw()
uzor_j(10)


def array_init(array_in, st): #Функция для визуализиции осей Ох и Оy
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st): # Функция ставит 1 в клетках, соответсвующих нужным нам точкам на графике
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot): # Функция раскрашивает нужные нам точки(1) грфика красным, а поле без значений(0) белым
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


array_plot = [[0 for col in range(10)] for row in range(10)] #Задание пустой будующей координатной плоскости
result = [0 for i in range(10)] #Задание пустых значений для оси Oy

for i in range(10): # Заполнение оси Oy т.к. мой график y = x/3
    result[i] = i / 3


step = round(abs((result[9] - result[0])) / 9, 1)

# Вывод задания 3

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)
print()

# Задание 4

import csv
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')

    _16yo = 0
    _ne16yo = 0
    z = -1
    for row in list(books)[1:]:
        age = row[5]

        if int(age) == 16:
            _16yo += 1
        else:
            _ne16yo += 1

summa = _16yo + _ne16yo
a = _16yo * 100 // summa
b = _ne16yo * 100 // summa + 1

print("16+                              " + BLUE + '  ' * a + END + ' ' + str(a) + '%')
print()
print("Остальные возрастные ограничения " + BLUE + '  ' * b + END + ' ' + str(b) + '%')
print()

#Допзадача, хочу заставить двигаться скобки (") ) )" -> " ) ) ")
import os
from time import sleep

t = 0.5
os.system('cls')
print(WHITE + '  ' * 1 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + END)
print(' ' + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1+ WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 1 + END)
print(' ' + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1+ WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 1 + END)
print(' ' + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1+ WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 1 + END)
print(' ' + WHITE + '  ' * 1 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1+ WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + END)
sleep(t)
print()
os.system('cls')
print(WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 1 + END)
print(' ' + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 0 + END)
print(' ' + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 0 + END)
print(' ' + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 0 + END)
print(' ' + GREEN + '  ' * 0 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 1 + END)
sleep(t)
print()
os.system('cls')
print(GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 0 + END)
print(' ' + WHITE + '  ' * 1 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + END)
print(' ' + WHITE + '  ' * 1 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + END)
print(' ' + WHITE + '  ' * 1 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + END)
print(' ' + WHITE + '  ' * 0 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + WHITE + '  ' * 2 + GREEN + '  ' * 1 + END)
sleep(t)
print()
os.system('cls')
os.system('pause')




