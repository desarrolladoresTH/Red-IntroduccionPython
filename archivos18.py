#leerArchivo
with open("frases_famosas.txt","r") as archivo:
	for linea in archivo:
		print("=== Frase ====")
		print(linea)


#reemplazarContenido
notas = {
		"Nora": 87,
		"Gino": 100,
		"Loretto": 67,
		"Talina": 45
}
with open("data_estudiantes.txt", 'w') as archivo:
		for nombre, nota in notas.items():
				archivo.write(nombre + " - " + str(nota) +" \n")

with open("data_estudiantes.txt","r") as archivo:
	for linea in archivo:
		print("=== Alumno ====")
		print(linea)


#añadirContenido
nuevas_notas = {
				"Emily": 54,
				"anie1": 98,
				"Julienne": 78
}

with open("data_estudiantes.txt", 'a') as archivo:
		for nombre, nota in nuevas_notas.items():
			archivo.write(nombre + " - " + str (nota) + "\n")

with open("data_estudiantes.txt","r") as archivo:
	for linea in archivo:
		print("=== Alumno ====")
		print(linea)			