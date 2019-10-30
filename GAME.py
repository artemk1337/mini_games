#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time


m = int(input("Введите начальное число: "))
N = int(input("Введите конечное число: "))
while m >= N:
    N = int(input("Введите другое число, которое будет больше начального числа: "))
z = 0
count = 0
count1 = 0

mas = []

print("Все простые числа:", end=" ")
for i in range(m, N + 1):
    z = 0
    for k in range(1, i + 1):
        if i % k == 0:
            z = z + 1
    if z == 2:
        mas.append(i)
        if count > 0:
            print(", ", i, end=' ')
        else:
            print(" ", i, end=' ')
        count = count + 1
        count1 = count1 + i
print()
print("Количество простых числе в диапазоне от", m, "до", N, "=", count)
print("Сумма всех простых чисел в диапазоне от", m, "до", N, "=", count1)
print()

# -------------------------------------------ИГРА---------------------------------------

r = int(input("Давайте сыграем в одну интересную игру? Если хотите сыграть, введите цифру 1: "))

if r == 1:
    print("\n" * 400, end='')  # Отступ
    
    print("Правила игры: вам нужно назвать все простые числа в диапазоне от", m, "до", N,)
    print("в возрастающей последовательности; на ввод одного числа отводится 5 секунд. Удачи!")
    r = int(input("Чтобы продолжить, введите цифру 1: "))
    if r == 1:
        print("Пригтовьтесь...")
        time.sleep(2)
        print("Начали!")
        for i in range(0, count):
            start = time.time()
            r = int(input())
            if time.time() - start <= 5:
                if r == mas[i]:
                    if i == count - 1:
                        print("Вы победили!! Поздравляю!!!")
                    else:
                        print("Правильно, дальше")
                else:
                    print("Вы проиграли!")
                    break
            else:
                print("Вы не успели!")
                break
print()
print("Конец.")
time.sleep(3)
