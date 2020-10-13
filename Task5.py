newlist = [7, 5, 3, 3, 2]

a = 0
while a < 1:
    i = int(input('Введите новый элемент рейтинга. Для выхода из цикла наберите 0 '))
    if i != 0:
        newlist.append(i)
        newlist.sort(reverse=True)
        print('Новый рейтнг:', newlist)
        
    else:
        break
