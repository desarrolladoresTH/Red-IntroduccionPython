# concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ______________

#organización = "freeCodeCamp" 

#print("Aprende a programar con " + organización)
#print("Aprende a programar con {}".format(organización))
#print(f"Aprende a programar con {organización}") #f-String

#Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("verbo: ")
verbo2 = input("verbo: ")
sustantivo_plural = input("sustantivo plural: ")

madlib = f"¡programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)