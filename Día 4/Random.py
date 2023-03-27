from random import *
#Numero entero aleatorio
aleatorio = randint(1,50)
print(aleatorio)
#Numero con decimal aleatorio
aleatorio = uniform(1,5)
print(aleatorio)
aleatorio = round(uniform(1,5),1)
print(aleatorio)
#Numero decimal entre 0 y 1
aleatorio = random()
print(aleatorio)
#Seleccion aleatoria dentro de los elementos de una lista
colores = ["azul", "rojo", "verde", "amarillo"]
aleatorio = choice(colores)
print(aleatorio)
#Mezclar
numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)

'''
Práctica Random 1
Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena 
dicho valor en una variable llamada aleatorio
'''
from random import randint
aleatorio = randint(1,10)

'''
Práctica Random 2
Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena 
dicho valor en una variable llamada aleatorio
'''
from random import random
aleatorio = random()

'''
Práctica Random 3
Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, 
y almacena el nombre escogido en una variable llamada sorteo.
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
'''
from random import choice
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
