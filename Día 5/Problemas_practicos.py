'''
Ejercicio 1
Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de
valor intermedio.
'''

def devolver_distintos(num1,num2,num3):
    lista = [num1,num2,num3]
    suma = sum(lista)
    lista.sort()
    if suma > 15:
        return lista[2]
    elif suma < 10:
        return lista[0]
    else:
        return lista[1]

print(devolver_distintos(10,5,6))
print(devolver_distintos(1,3,2))
print(devolver_distintos(10,1,4))

'''
Ejercicio 2
Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra 
como parámetro, y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver 
['d','e','i','n','o','r','t']
'''
def letras_unicas(palabra):
    letras = []
    for letra in palabra.lower():
        if letra not in letras:
            letras.append(letra)
    letras.sort()
    return letras

print(letras_unicas("enTretenido"))

'''
Ejercicio 3
Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función 
es devolver True si en algún momento se ha ingresado al numero cero repetido dos veces 
consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''
def repetidos(*args):
    repetido = True
    anterior = 1
    for arg in args:
        if anterior == 0 and arg == 0:
            return repetido
        anterior = arg
    return not repetido
print(repetidos(2,5,5,8,84,0,0,59,98598,78))
print(repetidos(2,5,5,8,84,0,59,98598,78))

'''
Ejercicio 4
Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va 
desde cero hasta ese número incluido, y va a devolver la cantidad de números primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
'''
def primos(num):
    contador = 0
    for n in range (2,num):
        if num % n == 0:
            contador += 1
    if contador > 0:
        return False
    else:
        return True

def contar_primos(num):
    contador_primos = 0
    lista_primos = []
    for n in range(2,num):
        if primos(n) == True:
            contador_primos +=1
            lista_primos.append(n)
    print(lista_primos)
    return contador_primos

print(primos(7))
print(contar_primos(100))

