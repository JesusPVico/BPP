from functools import reduce
import pdb

# PRIMER EJERCICIO
lista_de_listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

def mayor(a,b):
    if a > b:
        return a
    else:
        return b

pdb.set_trace()
for i in range(len(lista_de_listas)):
    elemento_mayor = reduce(mayor,lista_de_listas[i])
    print(elemento_mayor)


