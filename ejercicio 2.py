"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""



largo_lista = int(input("Ingrese el largo de la lista: "))
lista = []
for i in range(largo_lista):
    numeros_lista = int(input("Ingrese numeros de la lista: "))
    lista.append(numeros_lista)

print("Lista:", lista)
save = 1
cont = 0
lista_resultados = []
for l in lista:
    temp = l
    lista.remove(l)
    for n in lista:
        save = save * n
    print("multiplicacion: ", save)
    lista_resultados.append(save)    
    lista.insert(cont, temp)
    cont = cont + 1
    save = 1

print("Lista con las multiplicaciones: ", lista_resultados)

