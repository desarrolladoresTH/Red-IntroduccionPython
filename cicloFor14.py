
#for 
for i in range(4):
	print(i)

#for iterables
for char in "Loops":
	print(char)

#Ejemplo con una lista
for num in [1, 2, 3]:
	print(num)

#Ejemplo con diccionario (solo las claves)
letras={"a":1, "b":2}
for clave in letras:
		print(clave)

#Ejemplo con diccionario(solo valores)
#metodo .values()
for valor in letras.values():
		print(valor)

#Ejemplo con diccionario(Pares Clave-Valor)
#método .items()
for clave, valor in letras.items():
		print(clave, valor)
