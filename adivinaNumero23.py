
import random

#x es el limite superior y el parametro para llamar a la funcion

def adivina_el_numero(x):
    print("====================")
    print("Bievenid@ al juego!")
    print("====================")
    print("Tu meta es advinar el número generado por la computadora")

    numero_aleatoreo = random.randint(1, x) #numero aleatorio entre 1 y X de la función
    
    prediccion = 0
    #mientras la prediccion no sea igual a numero_aleatorio
    while prediccion != numero_aleatoreo:
        #el usuario ingresa numero                   #f-String
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))

        if prediccion < numero_aleatoreo:
            print("intenta otra vez. Este numero es muy pequeño.")
        elif prediccion > numero_aleatoreo:
            print("Intenta otra vez. Este numero es muy grande.")
    print(f"¡Felicitaciones! Adivinaste el numero {numero_aleatoreo} correctamente")


adivina_el_numero(10)

