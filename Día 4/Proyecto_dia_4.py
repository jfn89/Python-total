from random import randint
jugador = input("¿Cuál es tu nombre?: ")

print(f"Bueno, {jugador}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")

intentos = 0
numero_maquina = randint(1,101)
numero_jugador = 0

while intentos < 8 and numero_jugador != numero_maquina:
    numero_jugador = int(input("Elegí un número: "))
    if numero_jugador < 1 or numero_jugador > 100:
        print("El numero ingresado no está permitido")
        intentos += 1
    elif numero_jugador < numero_maquina:
        print("El número ingresado es menor al número secreto")
        intentos += 1
    elif numero_jugador > numero_maquina:
        print("El número ingresado es mayor al número secreto")
        intentos += 1
    else:
        intentos += 1
        print(f"¡Ganaste {jugador}! Te llevó {intentos} intentos.")

if intentos == 8 and numero_jugador != numero_maquina:
    print(f"Lo siento {jugador}, te quedaste sin intentos, el numero secreto era {numero_maquina}.")