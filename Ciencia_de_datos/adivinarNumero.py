#Importar generador de aleatorios enteros
from random import randint
#Función que evalua si el jugador ganó o perdió y le asigna un puntaje
def puntaje(intentos,numIntentos,numero,respuesta):
    if (numero==respuesta):
        print("Felicitaciones ha ganado el juego :) Puntaje: ",numIntentos-intentos+1,"/",numIntentos)
    else:
        print("Se acabaron los intentos :(  Puntaje: ",0,"/",numIntentos)
    print(f"Respuesta correcta {respuesta}")


##Configuración del juego
limInf=0
limSup=99
numIntentos=10
respuesta=randint(limInf,limSup) #Generar aleatorio
#print(respuesta)##Para validar la respuesta en pruebas

##Inicio del juego
print(f"Bienvenido a continuación hemos generado un número entero entre {limInf} y {limSup}")
numero= int(input("Adivina el número: "))
intentos=1

while  intentos<numIntentos:
    if numero==respuesta:
        break
    print("Número incorrecto,intentos restantes:",numIntentos-intentos)
    numero=int(input("Adivina el número: "))
    intentos+=1
puntaje(intentos,numIntentos,numero,respuesta)

