lista = ["a", "b", "c"]
for letra in lista:
    print(letra)

lista = ["a", "b", "c", "d"]
for letra in lista:
    print("Letra: " + letra)

lista = ["a", "b", "c", "d"]
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista = ["Pablo", "Laura", "Fede", "Luis", "Julia"]
for nombre in lista:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print(mi_valor)

palabra = "python"
for letra in palabra:
    print(letra)

palabra = "python es genial"
for letra in palabra:
    print(letra)

for letra in "python":
    print(letra)

for letra in [1,2,3]:
    print(letra)

for letra in (1,2,3):
    print(letra)

for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)

dic = {"clave1":"a", "clave2":"b", "clave3":"c"}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for a,b in dic.items():
    print(a,b)

'''
Práctica Loop For 1
Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
Por ejemplo: "Hola María"
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
'''
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print("Hola " + alumno)
    # TODO: write code...

'''
Práctica Loop For 2
Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de 
la suma en una variable llamada suma_numeros:
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
'''
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    # TODO: write code...

'''
Práctica Loop For 3
Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables 
suma_pares y suma_impares respectivamente:
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 
cuando es impar
num % 2 == 0 (valores pares)
num % 2 == 1 (valores impares)
'''
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    modulo = numero % 2
    if modulo == 0:
        suma_pares = suma_pares + numero
    elif modulo == 1:
        suma_impares = suma_impares + numero