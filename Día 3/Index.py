mi_texto = "Esta es una prueba"
#Caracter ubicado en ese índice
resultado = mi_texto [0]
print(resultado)
resultado = mi_texto [9]
print(resultado)
#Caracter ubicado comenzando desde el final
resultado = mi_texto [-4]
print(resultado)
#Índice donde se encuentra ese caracter (de izquierda a derecha)
resultado = mi_texto.index("n")
print(resultado)
"""
resultado = mi_texto.index("x")
print(resultado)
Si quiero buscar un valor que no esta o está escrito distinto da error
"""
#Índice donde comienza esa cadena de caracteres (de izquierda a derecha)
resultado = mi_texto.index("prueba")
print(resultado)
#Si busco un caracter que está más de una vez indica el primer indice donde se encuentra
resultado = mi_texto.index("a")
print(resultado)
#Indicar desde dónde empezar a buscar
resultado = mi_texto.index("a",5)
print(resultado)
#Indicar desde y hasta dónde buscar (no incluye el indice donde termina)
resultado = mi_texto.index("a",5,11)
print(resultado)
#Índice donde se encuentra ese caracter (de derecha a izquierda)
resultado = mi_texto.rindex("a")
print(resultado)

'''
Práctica Método Index() 1
Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
'''
palabra = "ordenador"
resultado = palabra[4]
print(resultado)

'''
Práctica Método Index() 2
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
'''
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index ("práctica")
print(resultado)

'''
Práctica Método Index() 3
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
'''
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)
