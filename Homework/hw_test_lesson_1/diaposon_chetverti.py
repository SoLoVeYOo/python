# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти: '))

if a == 1 : print('Диапозон возможных координат: x > 0 и y > 0')
elif a == 2 : print('Диапозон возможных координат: x < 0 и y > 0')
elif a == 3 : print('Диапозон возможных координат: x < 0 и y < 0')
elif a == 4 : print('Диапозон возможных координат: x > 0 и y < 0')
else: print('Введено неверное число')