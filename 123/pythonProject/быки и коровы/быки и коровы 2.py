from random import choice
z = '0123456789'
x = ''.join(choice(z[1:10]) for _ in range(4))
n = 0
while n < 10:
    y = input("Введите четырёхзначное число: ")
    if len(y) !=4:
        print("Ошибка: число должно быть четырехзначным")
        continue
    if y[0] == '0':
        print("Ошибка: первая цифра не может быть 0")
        continue
    n += 1
    b = 0; c = 0
    for i in range(4):
        if x[i] == y[i]:
            b += 1
        elif y[i] in x:
            c += 1
    print(y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы')
    if b == 4:
        print('Вы победили за', n, 'ходов')
        break
else:
    print('Вы проиграли, загаданное число было', x)

