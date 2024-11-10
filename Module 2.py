first=int(input('Введите число:'))
second=int(input('Введите число:'))
third=int(input('Введите число:'))
if first==second==third:
    print('Вывести: 3')
elif first==second or second==third or third==first:
    print('Вывести: 2')
else:
    print('Вывести:0 ')