#listas
letras = ["a", "b", "c", "d"]
numeros = [5, 4, 3, 2, 1]
print(letras)
#acceder
print(letras[0])
print(letras[1])
print(letras[2])
print(letras[3])

#agregar
letras.append("e")
print(letras)

letras.insert(0, "A")
print(letras)

#remover
letras.remove("c")
print(letras)

#encontrar
print('a' in letras)
print('z' in letras)

#retornaIndice
print(letras.index('A'))

#cambiarElemento
letras [0] = -8
print(letras)

#algunosMetodos

#Permite contar cuantas veces se repite un elemento en una lista
print(letras.count(-8))

#nos permite extender una lista agregándoles los elementos de otra lista
letras.extend(numeros)
print(letras)

#elimina y retorna un elemento de la lista
print(letras.pop(0))
print(letras)

#reversa el orden actual de la lista
letras.reverse()
print(letras)

#ordena la lista en un orden especifico ascendente o descendente
numeros.sort()
print(numeros)


