# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

spisok = []
for j in input('Введите строки через пробел: ').split():
        spisok.append(j)
chislo = input('Введите целое число для поиска: ')

def poisk_sovpadeniy(a: list, b: str) -> True:
    # for i in a:
    #     if i == b:
    #         return True
    if b in a: return True

try:
    proverka = int(chislo)
    if poisk_sovpadeniy(spisok, chislo) == True:
        print(f'Число {chislo} присутствует в заданном списке')
    else: print(f'Число {chislo} не присутствует в заданном списке')
except: print(f'Ошибка! Введите целое число для поиска')