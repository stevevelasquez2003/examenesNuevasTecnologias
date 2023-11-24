"""
Escriba un programa que muestre una partida de dados entre dos jugadores, se debe
ingresar la cantidad de turnos que se van a jugar, cada jugador tira un dado. Si un jugador
saca un valor mayor que el otro, gana los puntos de ambos dados. Si los dos jugadores
sacan el mismo valor, ninguno recibe puntos. Si en el ultimo turno hay un empate, esos
puntos se pierden y termina la partida. Debe mostrar quien gana la partida, quien gana
cada turno y la puntuación acumulada por cada jugador.
Para el examen pueden usar la librería random (import random) y utilizar el método
random.randint(desde, hasta) que toma números enteros de forma aleatorias según rango
dado

"""

import random

def tirardado():
    return int(random.random() * 6) + 1

def jugardados():
    
    num_turnos = int(input("Ingrese la cantidad de turnos: "))

   
    puntajeprimerjugador = 0
    puntajesegundojugador = 0

    
    for turno in range(1, num_turnos + 1):
        
        dadoprimerjugador = tirardado()
        dadosegundojugador = tirardado()

     
        print(f"\nTurno {turno}:")
        print(f"Jugador 1: {dadoprimerjugador}")
        print(f"Jugador 2: {dadosegundojugador}")

        
        if dadoprimerjugador > dadosegundojugador:
            puntajeprimerjugador += dadoprimerjugador + dadosegundojugador
            print("Jugador 1 gana el turno!")
        elif dadosegundojugador > dadoprimerjugador:
            puntajesegundojugador += dadoprimerjugador + dadosegundojugador
            print("Jugador 2 gana el turno!")
        else:
            print("Empate. Ningún jugador gana puntos en este turno.")

        
        print(f"Puntuación acumulada:")
        print(f"Jugador 1: {puntajeprimerjugador}")
        print(f"Jugador 2: {puntajesegundojugador}")

    
    if puntajeprimerjugador > puntajesegundojugador:
        print("\n¡Jugador 1 gana la partida!")
    elif puntajesegundojugador > puntajeprimerjugador:
        print("\n¡Jugador 2 gana la partida!")
    else:
        print("\nLa partida termina en empate.")


jugardados()

