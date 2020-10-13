
newlist = list(map(str, input('Введите элементы списка через пробел ').split()))

j = 0
for i in range(int(len(newlist) / 2)):
    newlist[j], newlist[j + 1] = newlist[j + 1], newlist[j]
    j += 2

print(newlist)