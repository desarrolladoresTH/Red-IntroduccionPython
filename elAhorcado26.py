import string
import random
#importa palabras26 y utiliza la lista palabras en obtener palabra valida
from palabras26 import palabras 
#importa ahorcadoDiagramas26 y utiliza vidas_diccionario_visual
from ahorcadoDiagramas26 import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    #Seleccionar una palabra al azar de la lista de palabras valida
    #choice nos permite obtener un valor random de una lista
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
        #upper convierte la cadena a mayusculas
    return palabra.upper()   


def ahorcado():

    print("==================================")
    print("¡Bienvenid@ al juego del ahorcado!")
    print("==================================")

    palabra = obtener_palabra_valida(palabras)
                        #set() = conjunto que nos permite #guardar elementos sin elementos #repetidos
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) # no tiene Ñ
    letras_por_adivinar = set(palabra)
    vidas = 7   

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #join une un conjunto de y lo separa con espacios
        #Letras adivinadas
        #' '.join({'a', 'b'})


        #mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]#List comprehension
        #mostrar estado ahorcado
        print(vidas_diccionario_visual[vidas])
        #mostrar las letras separadas por guion
        print(f"palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoje una letra: ").upper()

        #si la letra escojida por el usuario esta en el 
        #abecedario y no está en el conjunto de letras
        #que ya se an ingresado se añade la letra al conjunto #de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #si la letra esta en la palabra?
            #si la letra esta en la palabra, quitar la letra del conjunto de letras pendiente por adivinar
            #si no esta en la aplabra quietar una vida en el usuario
        
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else: 
                vidas = vidas - 1
                print(f"\n Tu letra, {letra_usuario} no esta en la palabra")
        
        #si la letra escojida por el usuario ya fue ingresado
        elif letra_usuario in letras_adivinadas:
            print("\n Ya escogiste esa letra. Por favor escoje una letra nueva")
        else:
            print("\n Esta letra no es valida")    

        #El juego llega a esta linea cuando se adivina todas las letras de la palabra o cuando se agotan las vidas del jugador
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! perdiste. La palabra era: {palabra}")
    else:
        print(f"¡Ganasteee!, Adivinaste la palabra {palabra}")       

                
if __name__ == '__main__':
    ahorcado()
