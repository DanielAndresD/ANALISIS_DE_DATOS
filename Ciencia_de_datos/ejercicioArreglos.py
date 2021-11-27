import numpy as np

#Función para intercambiar elementos de un arreglo de una posición a otra
#Parámetros:
#arreglo: matriz de n dimensiones
#index1: posición del primer elemento a intercambiar
#index1: posición del segundo elemento a intercambiar
def intercambio(arreglo,index1,index2):
    matriz=arreglo.copy()
    elemento1=arreglo[index1][:]
    elemento2=arreglo[index2][:]
    print("-----------------------------------------------")
    print("Elementos a intercambiar:\n")
    print(f"Elemento1 en el índice {index1}\n{elemento1},\n intercambia con Elemento2 en el indice {index2}\n{elemento2}")
    print("-----------------------------------------------")
    matriz[index2][:]=elemento1[:]
    matriz[index1][:]=elemento2[:]
    return matriz
    
#Generar un arreglo tridimensional de tamaño 9x9x9 con los números enteros del 0 al 728.

#Arreglo de (9,9,9) con valores del 0 al 728
arregloInicial=np.arange(729).reshape(9,9,9)
print("-----------------------------------------------")
print("Arreglo (9,9,9) de 729 elementos (0-728)")
print(arregloInicial)
print("-----------------------------------------------")
#print(arreglo)
#Imaginar que el arreglo se divide en 27 arreglos de 3x3x3; desarrollar una función que permita intercambiar
#  la posición de dos de estos bloques, pasándole como argumento únicamente la identificación de los bloques a intercambiar (los bloques se deben identificar con números del 0 al 26)
arregloAjustado=np.resize(arregloInicial,(27,3,3,3))
print("-----------------------------------------------")
print("Arreglo (3,3,3) de 27 elementos")
print(arregloAjustado)
print("-----------------------------------------------")
#Ejecutar

#Indices para intercambio
index1=0
index2=2
print(f"Se intecrambian los elementos de la posicion{index1} y posicion {index2}")
arregloIntercambio=intercambio(arregloAjustado,index1,index2)
print("-----------------------------------------------")
print("Arreglo (3,3,3) de 27 elementos")
print(arregloAjustado)
print("-----------------------------------------------")



