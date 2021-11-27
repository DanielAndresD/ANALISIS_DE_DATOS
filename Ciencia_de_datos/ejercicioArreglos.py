import numpy as np

def intercambio(arreglo,pos1,pos2):
    print("--------------------------------------------------------------------------------")
    print("Elemento 1")
    m1=arreglo[pos1][:]
    print(m1)
    print("Elemento 2")
    m2=arreglo[pos2][:]
    print(m2)
    print("--------------------------------------------------------------------------------")
    arreglo[pos1][:]
    arreglo[pos2][:]=m1
    print(arreglo)
    #return arreglo
#Generar un arreglo tridimensional de tamaño 9x9x9 con los números enteros del 0 al 728.
arregloInicial=np.arange(729).reshape(9,9,9)
#print(arreglo)
#Imaginar que el arreglo se divide en 27 arreglos de 3x3x3; desarrollar una función que permita intercambiar la posición de dos de estos bloques, pasándole como argumento únicamente la identificación de los bloques a intercambiar (los bloques se deben identificar con números del 0 al 26)

nuevoArreglo=np.resize(arregloInicial,(27,3,3,3))
#print(nuevoArreglo[0])
#print("--------------------------------------------------------------------------------")
#print(nuevoArreglo[26])

arregloIntercambio=intercambio(nuevoArreglo,0,26)

