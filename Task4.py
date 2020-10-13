newlist = list(map(str, input('Введите несколько слов через пробел ').split()))

length = len(newlist)
for i in range(length):
    print(str(i + 1), newlist[i][:10])