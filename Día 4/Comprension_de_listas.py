palabra = "python"
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

lista = [letra for letra in palabra]
print(lista)

lista = [letra for letra in "python"]
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n/2 for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)

lista = [n if n * 2 > 10 else "no" for n in range(0,21,2)]
print(lista)

pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]
print(metros)

'''
Práctica Comprensión de Listas 1
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino 
correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas 
para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!
Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
valores = [1, 2, 3, 4, 5, 6, 9.5]
'''
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]

'''
Práctica Comprensión de Listas 2
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino 
correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas 
para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!
Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
valores = [1, 2, 3, 4, 5, 6, 9.5]
'''
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n%2 == 0]

'''
Práctica Comprensión de Listas 3
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino 
correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas 
para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!
Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores 
de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:
°C = (°F - 32) * (5/9)
o expresado de otro modo:
(grados_fahrenheit-32)*(5/9)
La lista de temperaturas es la siguiente:
temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius
'''
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n - 32) * (5/9) for n in temperatura_fahrenheit]