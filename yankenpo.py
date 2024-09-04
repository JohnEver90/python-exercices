#importando la libreria random para obtener valores aleatorios
import random


def run():

    
    #cpuchoice = valuecpu()
    option1 = "Piedra"
    option2 = "Papel"
    option3 = "tijera"


    attempts = int(input("Hola, ¿Cuántas veces desea jugar a YanKenPo? :"))

    #confirmacion de intentos limitado a 10.
    if attempts <11:
        print(f"Usted jugará {attempts} veces ¡Buena suerte!")
    else:
        print("Solo se permite jugar un máximo de 10 veces")

    #lógica de juego
    while attempts != 0:        
        
        
        attempts -=1

    #Obteniendo opcion de jugador
    def valueuser():
        useroption = int(input("Eliga su opción:\n Opción 1 para elegir Piedra.\n Opción 2 para elegir Papel.\n Opción 3 para elegir tijera.\n Opción 0 para terminar de jugar y salir.\n Eliga:"))
        return useroption
    
    #Obteniendo opcion de la CPU
    def valuecpu():
        cpuchoice= random.randint(1,3)
        return cpuchoice


if __name__ == "__main__":
    run ()