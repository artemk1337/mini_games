#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from random import randint
import time as tm
from sys import exit


# Ошибка
def err():
    if error >= 3:
        exit('Я отказываюсь с вами играть!!!!! Вы НЕВМЕНЯЕМЫ!!!!!')


# -----------------------------------
# Приветствие + start()
def hi():
    global N
    global error
    global steps
    sp = 1
    steps = 0
    while sp != 0:
        lk = (input('Добро пожаловать в игру "крестики-нолики"! Чтобы продолжить, нажмите клавишу "Enter".'))
        if (lk == ''):
            sp = 0
    N = 0
    instruction()
    while N < 3 or N > 99:
        N = int(input('Введите число, равное ширине поля, на котором вы хотите играть, не менее 3 и не более 99 '
                      '(пример: 4): '))
    anp()
    k = 0
    while (k != 99) and ((k < 1) or (k > 3)):
        k = int(input('Выберите сложность по 3-ёх бальной шкале, от 1 до 3 (пример: 3): '))
    if k == 99:
        superpower()
    error = k
    label()
    start()


# Сверхразум
def superpower():
    global N
    print()
    print('Вы слишком примитивны для этой игры!!! Вам никогда не победить!!!')
    wait()
    N = 99
    anp()
    for i in range(N):
        for k in range(N):
            a[i, k] = 'O'
    pl()
    print()
    tm.sleep(2)
    exit('ВЫ ПРОИГРАЛИ!!! '*5)


# Заполнение массива поля
def anp():
    global a
    global N
    a = np.empty((N, N), dtype=str)
    for i in range(N):
        for k in range(N):
            a[i, k] = str(' ')


# Выбор символа
def label():
    global lab
    global error
    i4 = 1
    lab1 = ['X', 'O', type(str)]
    lab2 = ['O', 'X', type(str)]
    while i4 != 0:
        lab = (input('Вы хотите играть играть Х или О? Введите соответствующую букву (En/Ru): '))
        if (lab == 'X') or (lab == 'Х') or (lab == 'х') or (lab == 'x'):
            lab = lab1
            i4 = 0
        else:
            if (lab == 'o') or (lab == 'о') or (lab == 'O') or (lab == 'О'):
                lab = lab2
                i4 = 0
            else:
                err()
                error += 1
                print('Введите верную букву!!!')
    print(f'Вы играете за {lab[0]}')


# Кто начинает первым
def start():
    global error
    k1 = 0
    while k1 == 0:
        k = input('Надо решить, кто начинает первым. Орел или решка? (пример: орел)')
        if (k == 'орел') or (k == 'решка'):
            k1 = 1
        else:
            err()
            error += 1
            print('Введите верное слово!!!')
    i = randint(0, 100)
    print('Монетка полетела!')
    wait()
    if i < 50:
        print('Увы, удача отвернулась от тебя... Соперник начинает первым')
        print()
        bot()
        tm.sleep(2)
    else:
        print('Да ты сегодня чёртов везунчик! Начинай!!!')
        tm.sleep(2)
        pl()


# Ожидание рандома
def wait():
    for i in range(10):
        print('.', end='')
        tm.sleep(0.3)
    print('.')
# -----------------------------------


# Вывод поля
def pl():
    print('    1  ', end='')
    for i in range(1, N - 1):
        if i / 10 < 0.9:
            print(f' {i+1}  ', end='')
        if i / 10 >= 0.9:
            print(f'{i+1}  ', end='')
    if N-1 / 10 >= 0.9:
        print(N)
    if N-1 / 10 < 0.9:
        print(' ', end='')
        print(N)
    for i in range(1, N):
        zp1(i)
        zp2()
    zp1(N)


# Заполенние строк
def zp2():
    print('   ', end='')
    for k in range(N - 1):
        print('---|', end='')
    print('---')


# Заполенние строк
def zp1(d):
    if d >= 10:
        print(f'{d} ', end='')
    if d < 10:
        print(f' {d} ', end='')
    for k in range(N - 1):
        print(f' {a[d-1, k]} |', end='')
    print(f' {a[d-1, N-1]} ')


# Ход игрока
def player():
    global error
    global steps
    yes = 1
    while yes != 0:
        x = int(input('Введите номер столбца(пр.: 5): '))
        while x - 1 < 0 or x > N:
            err()
            print('Введите верный номер стобца, а не выдуманное число!!!!!')
            error += 1
        y = int(input('Введите номер строки(пр.: 4): '))
        while y - 1 < 0 or y > N:
            err()
            print('Введите верный номер строки, а не выдуманное число!!!!!')
            error += 1
        x -= 1
        y -= 1
        if (a[y, x] == lab[0]) or (a[y, x] == lab[1]):
            err()
            print('Выберете пустую ячейку!!!!!')
            error += 1
        else:
            a[y, x] = lab[0]
            yes = 0
    steps += 1
    pl()


# Ход соперника
def bot():
    yes = 1
    while yes != 0:
        i6 = 0
        i5 = randint(0, (N*N)-1)
        while i5 > N-1:
            i5 -= N
            i6 += 1
        if (a[i6, i5] != lab[0]) and (a[i6, i5] != lab[1]):
            a[i6, i5] = lab[1]
            yes = 0
    print()
    print('Ход соперника:')
    pl()


# Проверка на победу
def win(p1):
    global score
    score = 0
    # Горизонталь
    for i in range(N):
        for k in range(N-2):
            if (a[i, 0+k] == lab[p1]) and (a[i, 1+k] == lab[p1]) and (a[i, 2+k] == lab[p1]):
                score = 1
    # Вертикаль
    for i in range(N):
        for k in range(N-2):
            if (a[0+k, i] == lab[p1]) and (a[1+k, i] == lab[p1]) and (a[2+k, i] == lab[p1]):
                score = 1
    # Диагональ
    for i in range(N-2):
        for k in range(N-2):
            if (a[i, k] == lab[p1]) and (a[i+1, 1+k] == lab[p1]) and (a[i+2, k+2] == lab[p1]):
                score = 1
    for i in range(N-2):
        for k in range(N-1, 1, -1):
            if (a[i, k] == lab[p1]) and (a[i+1, k-1] == lab[p1]) and (a[i+2, k-2] == lab[p1]):
                score = 1


# Проверка на ничью
def draw():
    count = 0
    for i in range(N):
        for k in range(N):
            if (a[i, k] == lab[0]) or (a[i, k] == lab[1]):
                count += 1
    if count == N*N:
        print('У тебя ничья... Как же так?')
        quit()


# Результаты
def score1():
    global ttt1
    global steps
    ttt1 = round(- ttt1 + tm.time())
    print(f'Время, за которое вы прошли игру: {ttt1} сек')
    if steps == 1:
        print(f'За это время вы сделали {steps} шаг')
    if (steps > 1) and (steps < 5):
        print(f'За это время вы сделали {steps} шага')
    if steps > 4:
        print(f'За это время вы сделали {steps} шагов')


# инструкция
def instruction():
    print('Правила просты: нужно собрать 3 подряд идущих символа по горизонтали, вертикали или '
          'диагонали вне зависимости от размера поля.')


def main():
    global error
    global score
    global ttt1
    hi()
    ttt1 = tm.time()
    for i in range(N*N):
        player()
        win(0)
        if score == 1:
            print()
            print('Вау! Ты настоящий профессионал!!! Моё почтение!!!')
            print()
            score1()
            tm.sleep(10)
            quit()
        draw()
        bot()
        win(1)
        if score == 2:
            print()
            print('Ты проиграл! Очень жаль!.. Но ничего страшного, повезёт в другой раз!')
            print()
            score1()
            tm.sleep(10)
            quit()
        draw()


main()

