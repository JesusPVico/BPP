# Autor: Jesús Antonio Patricio Vico
# Buenas Prácticas de Programación
# Lección 1

"""
APARTADO 1:
Implemente un programa que lea el contenido del fichero csv finanzas2020 y realice los
siguientes cálculos:
¿Qué mes se ha gastado más?
¿Qué mes se ha ahorrado más?
¿Cuál es la media de gastos al año?
¿Cuál ha sido el gasto total a lo largo del año?
¿Cuáles han sido los ingresos totales a lo largo del año?
Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año

APARTADO 2:
Haciendo uso de excepciones, haga las siguientes comprobaciones:
● Compruebe que el fichero existe y que tiene 12 columnas, una para
cada mes del año.
● Para cada mes compruebe que hay contenido.
● Compruebe que todos los datos son correctos. De no haber un dato
correcto, el programa debe saber actuar en consecuencia y continuar
con su ejecución.
"""

# Importamos las librerías necesarias para el programa
import pandas as pd
import numpy as np

# En primer lugar leemos el fichero csv y comprobamos que no haya error en la lectura
try:
    finanzas2020 = pd.read_csv("finanzas2020.csv", sep="\t")
except IOError as err:
    print("No encuentro el fichero o no puedo leerlo. Error: ", err)
else:
    print("Se ha leído el fichero correctamente. Continuamos con el resto del programa.")

# También se comprueba que el número de columnas sea el correcto (12)
# Definimos la clase del error
class Error(Exception):
    pass

class ValorColumnasIncorrecto(Error):
    pass

class ColumnaVacia(Error):
    pass

try:
    if(finanzas2020.shape[1]!=12):
        raise ValorColumnasIncorrecto
except ValorColumnasIncorrecto:
    print("El número de columnas es incorrecto.")
else:
    print("El número de columnas es correcto. Continuamos con el resto del programa.")

# Ahora comprobamos que hay contenido para cada uno de los meses
try:
    for i in range(0, finanzas2020.shape[1]):
        if(len(finanzas2020.iloc[:,i])<1):
            raise ColumnaVacia
except ColumnaVacia:
    print("Hay algún mes sin contenido.")
else:
    print("Todos los meses tienen contenido. Continuamos con el resto del programa.")

# Lo siguiente es comprobar que los datos sean correctos. 
# Leemos todos los datos y comprobamos que sean enteros
# Si no lo son ponemos un 0 en la celda correspondiente

# Lo voy haciendo para cada mes
# ENERO
enero = finanzas2020["Enero"]
try:
    for i in range(0, len(enero)):
        numero=enero[i]
        if(numero[0]!="'"):
            enero[i]=int(enero[i])
        else:
            enero[i]=0
except ValueError as err:
    print("El dato no es correcto. Error: ", err)

# FEBRERO
febrero = finanzas2020["Febrero"]

# MARZO
marzo = finanzas2020["Marzo"]

# ABRIL
abril = finanzas2020["Abril"]

# MAYO
mayo = finanzas2020["Mayo"]

#JUNIO
junio = finanzas2020["Junio"]

#JULIO
julio = finanzas2020["Julio"]
while type(julio[len(julio)-1])!=int:
    try:
        for i in range(0, len(julio)):
                julio[i]=int(julio[i])

    except ValueError as err:
        print("El dato no es correcto. Error: ", err)
        julio[i]=0

#AGOSTO
agosto = finanzas2020["Agosto"]

#SEPTIEMBRE
septiembre = finanzas2020["Septiembre"]
while type(septiembre[len(septiembre)-1])!=int:
    try:
        for i in range(0, len(septiembre)):
                septiembre[i]=int(septiembre[i])

    except ValueError as err:
        print("El dato no es correcto. Error: ", err)
        septiembre[i]=0

#OCTUBRE
octubre = finanzas2020["Octubre"]
while type(octubre[len(octubre)-1])!=int:
    try:
        for i in range(0, len(octubre)):
                octubre[i]=int(octubre[i])

    except ValueError as err:
        print("El dato no es correcto. Error: ", err)
        octubre[i]=0

#NOVIEMBRE
noviembre = finanzas2020["Noviembre"]
while type(noviembre[len(noviembre)-1])!=int:
    try:
        for i in range(0, len(noviembre)):
                noviembre[i]=int(noviembre[i])

    except ValueError as err:
        print("El dato no es correcto. Error: ", err)
        noviembre[i]=0

#DICIEMBRE
diciembre = finanzas2020["Diciembre"]


# REALIZAMOS LOS CÁLCULOS CON LOS DATOS CORRECTOS
# Vector con los meses
columnas = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
            "Junio", "Julio", "Agosto", "Septiembre", 
            "Octubre", "Noviembre", "Diciembre"]

datos_correctos = np.array([enero,febrero,marzo,abril,mayo,junio,
                    julio,agosto,septiembre,octubre,noviembre,diciembre])

print("\n")
# ¿Qué mes se ha gastado más?
vector_gastos = [0]*12
for i in range(0, len(vector_gastos)):
    gasto=0
    for j in range(0,datos_correctos.shape[1]):
        if datos_correctos[i,j]<0:
            gasto = gasto + datos_correctos[i,j]
    
    vector_gastos[i]=gasto

mayor_gasto = min(vector_gastos)
mes = vector_gastos.index(mayor_gasto)
print(f"El mes en el que más se ha gastado ha sido {columnas[mes]}")

print("\n")
#¿Qué mes se ha ahorrado más?
vector_ahorro = [0]*12
for i in range(0, len(vector_ahorro)):
    ahorro=0
    for j in range(0,datos_correctos.shape[1]):
            ahorro = ahorro + datos_correctos[i,j]
    
    vector_ahorro[i]=ahorro

mayor_ahorro = max(vector_ahorro)
mes = vector_ahorro.index(mayor_ahorro)
print(f"El mes en el que más se ha ahorrado ha sido {columnas[mes]}")

print("\n")
#¿Cuál es la media de gastos al año?
print(f"La media de gastos al año fue {sum(vector_gastos)/12}")

print("\n")
#¿Cuál ha sido el gasto total a lo largo del año?
print(f"El gasto total a lo largo del año fue {sum(vector_gastos)}")

print("\n")
#¿Cuáles han sido los ingresos totales a lo largo del año?
vector_ingresos = [0]*12
for i in range(0, len(vector_ingresos)):
    ingreso=0
    for j in range(0,datos_correctos.shape[1]):
        if datos_correctos[i,j]>0:
            ingreso = ingreso + datos_correctos[i,j]
    
    vector_ingresos[i]=ingreso

print(f"Los ingresos totales a lo largo del año han sido  {sum(vector_ingresos)}")
