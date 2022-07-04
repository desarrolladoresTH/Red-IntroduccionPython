#

import random 
import time # medir tiempo


def busqueda_ingenua(lista, objetivo):#retorna el indice de la lista
    for i in range(len(lista)):#range(len(lista)) -> 0,1,2,3,.....len(lista) -1
        if lista[i] == objetivo:
            return i
    return -1


#mi_lista=[1, 3, 5, 10, 12]
#print(busqueda_ingenua(mi_lista, 15))

def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 #0 inicio de la lista
    if limite_superior is None:
        limite_superior= len(lista)-1 #Final de la lista

    if limite_superior < limite_inferior:
        return -1

            #recursiva
            #// division entera
    punto_medio = (limite_inferior + limite_superior)// 2
            
            # [1, 3, 5, 10, 12]
            #  0  1  2  3   4
            #punto medio = (0+4) // 2 = 4 // 2 = 2(indice)
            #punto medio = 5 (indice 2)
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo,punto_medio +1, limite_superior)    



if __name__== '__main__':
    # mi_lista =[1, 3, 5, 10, 12]
    #print(busqueda_binaria(mi_lista, 7))
    
    #crear una lista ordena con 10000 numeros randoms
    tamaño = 20000
    conjunto_inicial = set() #conjunto sin elementos repetidos

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
        #sorted= ordena ascendente y la retorna a una variable
        #convierte conjunto en una lista
    lista_ordenada= sorted(list(conjunto_inicial)) 
    
    #medir tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print (f"tiempo de busqueda ingenua {fin - inicio} segundos")

    #medir tiempo de busqueda binaria
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print (f"tiempo de busqueda binaria {fin - inicio} segundos")