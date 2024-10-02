import time

print('О чём вам напомнить')
text = input('Введите ваше напоминание')
print('Через сколько минут напоминть?')

'''Перевод времени. Храним время через какое время нужно показать напоминание'''
local_time = float(input())
local_time = local_time * 60

time.sleep(local_time)
print(text)

######################################################################################################################
import time
from threading import Thread

def SleepMe(i):
    print('Поток %i засыпает на 5 секунд. \n' %i)
    time.sleep(5)
    print('Поток %i сейчас проснулся. \n' %i)
'''Цикл вне функции!!!'''
for i in range(10):
    time.sleep(3)
    th = Thread(target=SleepMe, args=(i,))
    th.start()
######################################################################################################################
import time
from threading import Thread
def remind():
    print('О чём вам напомнить')
    text = input('Введите ваше напоминание')
    print('Через сколько минут напоминть?')

    '''Перевод времени. Храним время через какое время нужно показать напоминание'''
    local_time = float(input())
    # local_time = local_time * 60

    time.sleep(local_time)
    print(text)

th = Thread(target=remind, args=())
th.start()

time.sleep(10)
print('пока поток работает, мы можем сделать что нибудь ещё\n')
######################################################################################################################
from  threading import  Thread
import time

def print_numders():
    for i in range(5):
        print(f'Numder:{i}')
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(f'Letter: {letter}')
        time.sleep(1)

th = Thread(target=print_numders)
th1 = Thread(target=print_letters)
"""Старт"""
th.start()
th1.start()
"""Ждём завершение аргументов"""
th.join()
th1.join()
######################################################################################################################
