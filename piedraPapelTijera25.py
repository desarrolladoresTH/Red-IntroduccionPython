import random


def jugar():
    #lower va a convertir todos los caracteres en minusculas
    usuario = input(f"Escoge una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera. \n").lower()
    #choice nos permite obtener un valor random de una lista
    computadora = random.choice(['pi', 'pa', 'ti'])
    print("La computadora eligio: "+computadora)

    if usuario == computadora:
        return "!Empate¡"

    if gano_el_jugador(usuario, computadora):
        return "!Ganaste¡"   

    return "!Perdiste¡"        


def gano_el_jugador(jugador, oponente):
    #Retornar True si gana el jugador
    #Piedra gana a tijera (pi > ti)
    #Tijera gana a Papel (ti > pa)
    #Papel gana a piedra (pa > pi)
    if ((jugador == 'pi' and oponente == 'ti') or 
        (jugador == 'ti' and oponente == 'pa') or
        (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False  

print(jugar())


