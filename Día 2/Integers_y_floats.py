mi_numero = 1
print(mi_numero)
print(type(mi_numero))
mi_numero = 1 + 3
print(mi_numero)
print(type(mi_numero))
mi_numero = 1 + 3
print(mi_numero + mi_numero)
print(type(mi_numero))
mi_numero = 5.8
print(mi_numero)
print(type(mi_numero))
mi_numero = 5.8
mi_numero = mi_numero + mi_numero
print(mi_numero)
print(type(mi_numero))
mi_numero = 5 + 5.8
print(mi_numero)
print(type(mi_numero))
edad = input("Dime tu edad: ")
print("Tu edad es " + edad)
print(type(edad))
print(edad + edad) #Concatena porque son 2 str
"""nueva_edad = 1 + edad
print("Vas a cumplir " + nueva_edad)
Nos dará error porque no pueden operarse un str y un int"""

'''
Práctica con Integers
Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.
Imprime el tipo de dato de dicha variable.
'''
num_entero = 30
print(type(num_entero))

'''
Práctica con Floats
Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.
Imprime el tipo de dato de dicha variable.
'''
num_decimal = 11.11
print(type(num_decimal))

'''
Práctica con Tipos de Datos Numéricos
¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.
Para ello, crea dos variables:
num1 = 7.5
num2 = 2.5
A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.
Realiza el mismo ejercicio en PyCharm para ver el resultado. ¿Coindice con lo que esperabas?
'''
num1 = 7.5
num2 = 2.5
print(type(num1 + num2))
