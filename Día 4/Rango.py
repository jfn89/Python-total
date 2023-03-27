#Por defecto empieza en 0 y no es inclusivo
for numero in range(5):
    print(numero)
#Se puede elegir entre que numeros quiero el rango
for numero in range(1,5):
    print(numero)
for numero in range(20,31):
    print(numero)
#Puedo elegir cada cuanto toma un numero
for numero in range(20,31,2):
    print(numero)
for numero in range(20,31,3):
    print(numero)
#Puedo listar un rango
lista = list(range(1,101))
print(lista)

'''
Práctica Rango 1
Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable 
mi_lista.
'''
mi_lista = list(range(2500, 2586))

'''
Práctica Rango 2
Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 
desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
'''
mi_lista = list(range(3, 301, 3))

'''
Práctica Rango 3
Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el 
resultado en una variable llamada suma_cuadrados.
Para ello:
Crea un rango de valores que puedas recorrer en un loop
Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables 
intermedias (de manera opcional).
Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.
'''
numeros = range(1, 16)
suma_cuadrados = 0
for numero in numeros:
    suma_cuadrados = suma_cuadrados + numero ** 2