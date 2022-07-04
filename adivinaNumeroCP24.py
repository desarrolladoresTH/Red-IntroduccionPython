import random

#x es el limite superior y el parametro para llamar a la funcion
def adivina_el_numero_computadora(x):
    print("==========================")
    print("¡Bienvenid@ al juego!")
    print("==========================")
    print(f"selecciona un número entre 1 y {x} para que la computadora intente adivinarlo......")
    limite_inferior=1 
    limite_superior=x
    respuesta = ""
    while respuesta != "c":
        # Generar prediccion
        #si limite_inferior es distinto a limite_superior
        if limite_inferior != limite_superior: #[1, x]
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion= limite_inferior

        #obtener respuesta
        #lower va a convertir todos los caracteres en minusculas
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
        #Intervalo inicial. [1, 10]
        #Prediccion:  6
        # respuesta: "a"
        #intervalo [1, 5] 
            limite_superior = prediccion-1
        elif respuesta == "b":
        #Intervalo inicial. [1, 10]
        #Prediccion:  6
        # respuesta: "b"
        #intervalo [7, 10]
            limite_inferior = prediccion + 1
    print(f"La computadora adivino tu numero correctamente: {prediccion} ")    




adivina_el_numero_computadora(10)