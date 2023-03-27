num1 = 20
num2 = 30.5
print(type(num1))
print(type(num2))
num1 = num1 + num2 #Convierte automáticamente a float
print(type(num1))
print(type(num2))
num1 = 5.8
print(num1)
print(type(num1))
num2 = int(num1) #Convierte a int eliminando los decimales
print(num2)
print(type(num2))
edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)
"""
print("Tu nueva edad va a ser " + nueva_edad)
Dará error porque no puede concatenar un str con un int
"""

'''
Práctica con Conversiones 1
Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
'''
num1 = 7.5
num1 = int(num1)
print(type(num1))

'''
Práctica con Conversiones 2
Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
'''
num2 = 10
num2 = float(num2)
print(type(num2))

'''
Práctica con Conversiones 3
Suma los valores de num1 y num2.
No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().
'''
num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))