from random import choice
#Seleccion de palabra
def seleccion_palabra(lista):
    palabra = choice(lista)
    return palabra
#Tablero
def tablero(palabra):
    mostrar = []
    letras_palabra = []
    for letra in palabra:
        mostrar.append("_")
        letras_palabra.append(letra)
    print("".join(mostrar))
    return letras_palabra
#Ingreso de letra
def ingreso_usuario():
    ingreso = " "
    while ingreso not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        ingreso = input("Ingresá una letra: ").upper()
    return ingreso
#Verificacion de intento
def verificar(ingreso,palabra):
    if ingreso in palabra:
        return True
    else:
        return False
#Actualizar tablero
def actualizar_tablero(tablero,letras):
    mostrar = []
    for letra in tablero:
        if letra in letras:
            mostrar.append(letra)
        else:
            mostrar.append("_")
    print("".join(mostrar))
    return mostrar
#Ganar
def ganar(ingresos,palabra):
    if ingresos == palabra:
        print("Felicidades, ganaste!!!!")
#Perder
def perder(vidas,palabra):
    if vidas == 0:
        print(f"Mejor suerte la proxima vez! La palabra era {palabra}")

print("***********Juguemos al ahorcado***********")
vidas = 6
palabras = ["DINOSAURIO", "ARBOL", "CHOCLO", "MAR", "ABECEDARIO"]
palabra_secreta = seleccion_palabra(palabras)
pantalla_inicial = tablero(palabra_secreta)
letras_correctas = []
letras_incorrectas = []
actualizacion = []

while vidas > 0 and actualizacion!=pantalla_inicial:
    ingreso = ingreso_usuario()
    if verificar(ingreso,palabra_secreta) == True:
        letras_correctas.append(ingreso)
        actualizacion = actualizar_tablero(pantalla_inicial,letras_correctas)
        ganar(actualizacion,pantalla_inicial)
    else:
        letras_incorrectas.append(ingreso)
        vidas -= 1
        print(letras_incorrectas)
        perder(vidas,palabra_secreta)
