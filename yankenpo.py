#importando la libreria random para obtener valores aleatorios
import random


def run():
 
    #Confirmacion de intentos limitado a 10. Y manejando la excepcion de q no se un número y esté en el rango 1 -10
    def confirm():
        while True:
            try:
                attempts = int(input("Hola, ¿Cuántas veces desea jugar a YanKenPo? (un máximo de 10 veces): "))
                if 1 <= attempts <= 10:
                    return attempts
                else:
                    print("\nPor favor, ingresa un número entre 1 y 10.")
            except ValueError:
                print("\nError: Por favor, ingresa un número válido (desde 1, hasta un máximo de 10).")

    #Guardo el valor q retorna la confirmación de intentos
    intentos = confirm()

    #Mensaje de confirmación
    print(f"\nUsted jugará {intentos} veces ¡Buena suerte!")

    
    #Contadores score
    score_user = 0
    score_cpu = 0
    draw = 0

    #Bucle de encuentros a realizarse/Lógica de juego
    for i in range(1, intentos+1):
        #Obteniendo opcion de jugador
        def valueuser():
            while True:
                try:                
                    useroption = int(input("Eliga su opción: Opción 1 para elegir Piedra.\n Opción 2 para elegir Papel.\n Opción 3 para elegir tijera.\n Opción 0 para terminar de jugar y salir.\n Eliga: "))
                    if 0<= useroption <=3:
                        return useroption
                    else:
                        print("Por favor eliga una de las opciones dadas. 1,2 ó 3")
                    #Finalizando el programa
                    
                except ValueError:
                        print("Por favor ingrese un valor numérico válido, 1,2 ó 3")

        #Guardo el valor q retorna la opción del usuario
        userchoice = valueuser()

        #Obteniendo opcion de la CPU
        def valuecpu():
            cpuoption= random.randint(1,3)
            return cpuoption
        
        #Guardo el valor de la opcion de la CPU
        cpuchoice = valuecpu()

        #Finalizando el programa
        if userchoice == 0:
            print("Usted decidió dejar de jugar. Gracias por participar.")
            break

    #Lógica de juego
        #Casos donde el usuario gana
        if userchoice == 1 and cpuchoice == 3:
            print("Usted eligió piedra y la CPU eligió tijera.")
            print("Usted ganó, piedra le gana a tijera.")
            score_user +=1
        elif userchoice == 2 and cpuchoice == 1:
            print("Usted eligió papel y la CPU eligió piedra.")
            print("Usted ganó, papel le gana a piedra.")
            score_user +=1
        elif userchoice == 3 and cpuchoice == 2:
            print("Usted eligió tijera y la CPU eligió papel.")
            print("Usted ganó, tijera le gana a papel.")
            score_user +=1
        #Casos donde el usuario pierde
        elif userchoice == 1 and cpuchoice == 2:
            print("Usted eligió piedra y la CPU eligió papel.")
            print("Usted perdió, papel le gana a piedra.")
            score_cpu +=1
        elif userchoice == 2 and cpuchoice == 3:
            print("Usted eligió papel y la CPU eligió tijera.")
            print("Usted perdió, tijera le gana a papel.")
            score_cpu +=1
        elif userchoice == 3 and cpuchoice == 1:
            print("Usted eligió tijera y la CPU eligió piedra.")
            print("Usted perdió, piedra le gana a tijera.")
            score_cpu +=1
        #Casos donde se empata
        elif userchoice == 1 and cpuchoice ==1:
            print("Ambos jugadores eligieron piedra, ha sido un empate.")
            draw +=1
        elif userchoice == 2 and cpuchoice ==2:
            print("Ambos jugadores eligieron papel, ha sido un empate.")
            draw +=1
        elif userchoice == 3 and cpuchoice ==3:
            print("Ambos jugadores eligieron tijera, ha sido un empate.")
            draw +=1

    print(score_user)
    print(score_cpu)
    print(draw)

            
        
        


    

if __name__ == "__main__":
    run ()