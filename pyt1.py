import time

print('О чём вам напомнить')
text = input('Введите ваше напоминание')
print('Через сколько минут напоминть?')

'''Перевод времени. Храним время через какое время нужно показать напоминание'''
local_time = float(input())
local_time = local_time * 60

time.sleep(local_time)
print(text)


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
