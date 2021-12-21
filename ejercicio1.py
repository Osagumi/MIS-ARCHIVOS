#

import random

k = random.randint(1,50)
list = []
print("numero azar: ", k)

for i in range(0,4):
    num = random.randint(0,40)
    list.append(num)

print("lista 1: ", list)
save = 0
cont = 0
list2 = []
for l in list:
    temp = l
    list.remove(l)
    print("asi queda lista: ", list)
    for i in list:
        save = temp + i
        list2.append(save)
        print("asu}i queda lista 2: ", list2) 
    list.insert(cont, temp)
    cont = cont + 1
print ("lista 2: ", list2)

for j in list2:
    if k == j:
        print("Coincidencia")
        k = 0   