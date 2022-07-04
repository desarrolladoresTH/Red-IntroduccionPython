#función
def mostrar_mensaje():
		print("!Hola, Mundo¡")

mostrar_mensaje()


#funciónParámetro
def mostrar_doble(num):
		print(num*2)

num = int(input("ingrese un numero: "))
mostrar_doble(num)


#funciónVariosParámetros
def sumar(x, y):
		print(x + y)

x = int(input("ingrese un numero: "))
y = int(input("ingrese otro numero: "))
sumar(x, y)       

#funciónReturn
def sumar2(x2, y2):
    return x + y

x2 = int(input("ingrese un numero: "))
y2 = int(input("ingrese otro numero: "))
sumar(x2, y2)