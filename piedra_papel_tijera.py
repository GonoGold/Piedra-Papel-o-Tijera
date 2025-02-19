# -*- coding: utf-8 -*-
"""piedra_papel_tijera.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iN-ZBqFgchyXhBzL2e9biR1LXSA0t2Fy

#Piedra Papel O tijera
"""

import random

def imprimir_resultado_final(ganadas_usuario, ganadas_ordenador):
    print("\nResultados finales:")
    print(f"Usuario ganó {ganadas_usuario} veces.")
    print(f"Ordenador ganó {ganadas_ordenador} veces.")

    if ganadas_usuario > ganadas_ordenador:
        print("¡Felicidades! Has ganado el juego.")
    elif ganadas_usuario < ganadas_ordenador:
        print("Lo siento, el ordenador ha ganado el juego.")
    else:
        print("El juego terminó en empate.")
def jugar_ronda(opciones):
    usuario = input("Elige entre piedra, papel o tijera: ").lower()
    ordenador = random.choice(opciones)

    if usuario not in opciones:
        print("Entrada no válida. Elige piedra, papel o tijera.")
        return None, None

    print(f"El ordenador eligió: {ordenador}")

    if usuario == ordenador:
        print(f"Empate, ambos eligieron {usuario}.")
        return None, None
    elif (usuario == "tijera" and ordenador == "papel") or \
         (usuario == "piedra" and ordenador == "tijera") or \
         (usuario == "papel" and ordenador == "piedra"):
        print(f"Has ganado. {usuario} vence a {ordenador}.")
        return True, False
    else:
        print(f"Has perdido. {ordenador} vence a {usuario}.")
        return False, True
def main():
    opciones = ["tijera", "papel", "piedra"]

    while True:
        intentos = 5
        ganadas_usuario = 0
        ganadas_ordenador = 0

        while ganadas_usuario < 3 and ganadas_ordenador < 3 and (ganadas_usuario + ganadas_ordenador) < intentos:

            resultado_usuario, resultado_ordenador = jugar_ronda(opciones)

            if resultado_usuario is None and resultado_ordenador is None:
                continue

            if resultado_usuario:
                ganadas_usuario += 1
            if resultado_ordenador:
                ganadas_ordenador += 1

        imprimir_resultado_final(ganadas_usuario, ganadas_ordenador)

        jugar_nuevamente = input("\n¿Quieres jugar otra vez? (sí/no): ").lower()
        if jugar_nuevamente != "sí":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break


main()