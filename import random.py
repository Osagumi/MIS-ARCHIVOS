import random

k = random.randint(0,50)
list = [list]

for i in range(0,4):
    num = random.randint(0,40)
    list.append(num)

print(list)
save = 0
list2 = []
list3 = []
for l in list:
    temp = l
    list.pop(list.index(l))
    for i in list:
        save = temp + i
        list2.append(save)
    list.append(temp)    

for j in list2:
    while k == j:
        print("Coincidencia")
        k = 0   