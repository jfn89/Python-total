texto = "Este es el texto de Federico"
#Mayusculas
resultado = texto.upper()
print(resultado)
resultado = texto[2].upper()
print(resultado)
#Minusculas
resultado = texto.lower()
print(resultado)
#Separar (lo transforma en lista, tomando como separador los espacios o el caracter que pase como parámetro)
resultado = texto.split()
print(resultado)
resultado = texto.split("t")
print(resultado)
#Unir (une elementos de una lista)
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " "
f = e.join([a,b,c,d])
print(f)
g = "-".join([a,b,c,d])
print(g)
#Buscar (Busca el caracter y devuelve el índice, si no encuentra el caracter devuelve -1)
resultado = texto.find("s")
print(resultado)
resultado = texto.find("g")
print(resultado)
#Reemplazar, busca el primer parámetro y lo reemplaza por el segundo
resultado = texto.replace("Federico","todos")
print(resultado)
resultado = texto.replace("e","x")
print(resultado)

'''
Práctica Métodos de String 1
Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
'''
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

'''
Práctica Métodos de String 2
Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de 
listas/strings, y muestra en pantalla el resultado.
'''
lista_palabras = ["La","legibilidad","cuenta."]
lista = " ".join(lista_palabras)
print(lista)

'''
Práctica Métodos de String 3
Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."
los siguientes pares de palabras:
"difícil" --> "fácil"
"mala" --> "buena"
y muestra en pantalla la frase con ambas palabras modificadas.
'''
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala","buena"))