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

# SEGUNDO EJERCICIO
elementos =  [3, 4, 8, 5, 5, 22, 13]

def es_primo(n):
    primo=True

    for i in range(2,n-1):
        if(n%i == 0):
            primo = False

    return primo

primos = list(filter(es_primo, elementos))
print(primos)
