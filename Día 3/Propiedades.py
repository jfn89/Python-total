"""
nombre = "Carina"
nombre [0] = "K"
print(nombre)
nombre = "Karina"
Da error porque los str no soportan asignacion de items, para esto puedo modificar el contenido de la variable
"""
#Concatena
n1 = "Kari"
n2 = "na"
print(n1+n2)
print(n1*10)
#Saltos de linea
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)
#Consultar si hay o no hay determinado sub str en el str
print("agua" in poema)
print("sol" in poema)
print("sol" not in poema)
print("agua" not in poema)
#Consultar el largo de un str
print(len(poema))
poema = "hola mundo!"
print(len(poema))

'''
Práctica Propiedades de Strings 1
Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son 
multiplicables y puedes realizar esta actividad de forma simple y elegante.
'''
a = "Repetición"
print(a*15)

'''
Práctica Propiedades de Strings 2
Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
Tierra mojada,
mis recuerdos de viaje
entre las lluvias
'''
haiku = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print("agua" not in haiku)

'''
Práctica Propiedades de Strings 3
Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
'''
print(len("electroencefalografista"))