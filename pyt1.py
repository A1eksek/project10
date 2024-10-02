import time

print('О чём вам напомнить')
text = input('Введите ваше напоминание')
print('Через сколько минут напоминть?')

'''Перевод времени. Храним время через какое время нужно показать напоминание'''
local_time = float(input())
local_time = local_time * 60

time.sleep(local_time)
print(text)
