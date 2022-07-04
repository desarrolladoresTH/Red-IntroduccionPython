#diccionario
edades = {"Gino": 15, "Nora": 45}

#acceder
print(edades["Gino"])
print(edades["Nora"])
#Otra manera:
print(edades.get("Gino"))

#Añadir y Modificar 
#si la clave es nueva
edades["Talina"] = 67
print(edades)
#si la clave ya existe
edades["Gino"] = 17
print(edades)

#Remover
del edades["Talina"]
print(edades)

#revisarExistencia
print("Gino" in edades)
print("Emily" in edades)
print("Nora" in edades)


