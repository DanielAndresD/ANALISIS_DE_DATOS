#Juego de adivinanza numeros aleatorios
#@autor: Daniel Andrés Dávila Lesmes
#@Codigo: 20161015108
#@Asignatura: Introducción a la Ciencia de datos 2021-3
#@Correo: dadavilal@correo.udistrital.edu.co

#Importar generador de aleatorios enteros
from random import randint
##Función para dar pistas
def pistas(numero,respuesta):
    desviacion= numero-respuesta
    mensaje="El numero es "
    #Sentencia de rango
    if abs(desviacion)<=5:
        mensaje+="un poquito "
    elif abs(desviacion)<=10:
        mensaje+="un poco "
    elif abs(desviacion)<=20:
        mensaje=mensaje
    else:
        mensaje+="mucho "
    #Comparativo si es mayor o menor
    if desviacion >0:
        mensaje+="menor"
    else:
        mensaje+="mayor"
    return mensaje

##Configuración del juego
limInf=0
limSup=99
numIntentos=10

##Inicio del juego
print(f"Bienvenido a continuación hemos generado un número entero entre {limInf} y {limSup}")
respuesta=randint(limInf,limSup) #Generar aleatorio
##print(respuesta)##Para validar la respuesta en pruebas

##Inicializar variables del bucle
intentos=0

## ciclo para recibir las respuestas con n numero de intentos
while  intentos<numIntentos:
    numero=int(input("Adivina el número: "))#Captura el valor del usuario
    #Romper el bucle en caso de ganar
    if numero==respuesta:
        print("Felicitaciones ha ganado el juego :)")
        break
    intentos+=1
    print("Número incorrecto,intentos restantes:",numIntentos-intentos)
    print(pistas(numero,respuesta))
else:
    print("Se acabaron los intentos :(")
print(f"Respuesta correcta {respuesta}")
print("Puntaje: ",numIntentos-intentos,"/",numIntentos)

