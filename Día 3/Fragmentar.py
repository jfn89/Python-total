texto = "ABCDEFGHIJKLM"
fragmento = texto [2]
print(fragmento)
#Caracteres desde y hasta donde se indica (no se incluye el caracter del indice final)
fragmento = texto [2:5]
print(fragmento)
#Caracteres desde el índice indicado y hasta el final
fragmento = texto [2:]
print(fragmento)
#Caracteres desde el comienzo y hasta el índice indicado (no se incluye ese caracter)
fragmento = texto [:5]
print(fragmento)
#Caracteres desde y hasta donde se indica (no se incluye el caracter del indice final) cada la cantidad de caracteres que indique
fragmento = texto [2:10:2]
print(fragmento)
fragmento = texto [2:10:3]
print(fragmento)
fragmento = texto [::3]
print(fragmento)
#Cadena al revés
fragmento = texto [::-1]
print(fragmento)
fragmento = texto [::-2]
print(fragmento)

'''
Práctica Sub-Strings 1
Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
"Controlar la complejidad es la esencia de la programación"
Pista: "Controlar" tiene un largo de 9 caracteres.
'''
frase = "Controlar la complejidad es la esencia de la programación"
resultado = frase[:9]
print(resultado)

'''
Práctica Sub-Strings 2
Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
"Nunca confíes en un ordenador que no puedas lanzar por una ventana"
'''
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado = frase[8::3]
print(resultado)

'''
Práctica Sub-Strings 3
Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
'''
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = frase[::-1]
print(resultado)
