mi_tuple = (1,2,3,4)
print(type(mi_tuple))
t = (5,5.6,"ff")
print(mi_tuple[0])
print(mi_tuple[-2])
"""
Si quiero modificar un valor en la tupla me va a dar error
mi_tuple[0] = 5
print(mi_tuple)
"""
mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2][0])
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))
#Puedo asignar los elementos de un tuple a variables siempre que coincidan las cantidades
t = (1,2,3)
x,y,z = t
print(x,y,z)
t = (1,2,3,1)
#Largo
print(len(t))
#Cantidad de veces que aparece un elemento
print(t.count(1))
#Posicion del elemento
print(t.index(2))

'''
Práctica Tuples 1
Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el 
resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
'''
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

'''
Práctica Tuples 2
Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
'''
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

'''
Práctica Tuples 3
Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
mi_tupla = (1, 2, 3, 4)
'''
mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
