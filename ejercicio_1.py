import os
lista_numeros = [18, 50, 210, 80, 145, 333, 70, 30]
def multiplo_y_menor(i):
    for i in range(0, len(lista_numeros)-1):
        if i %10 == 0 and i < 200:
            return i

def mayor_300(i):
    for i in range(0, len(lista_numeros)-1):
        if i > 300:
            break

def organizar_merge_sort(i):
    return i.sort

def devolver(i):
    for i in lista_numeros:
        if i == 145:
            print(150)
        else:
            print(-1)
        return devolver