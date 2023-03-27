mi_lista = ["a", "b", "c"]
otra_lista =  ["hola", 55, 6.1]
print(type(mi_lista))
#Cantidad de elementos
resultado = len(mi_lista)
print(resultado)
#Elementos por separado
resultado = mi_lista[0]
print(resultado)
resultado = mi_lista[0:2]
print(resultado)
#Concatenar
mi_lista2 = ["d", "e", "f"]
print(mi_lista+mi_lista2)
print(mi_lista)
print(mi_lista2)
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)
#Modificar un elemento
mi_lista3[0] = "alfa"
print(mi_lista3)
#Agregar un elemento
mi_lista3.append("g")
print(mi_lista3)
#Eliminar un elemento
mi_lista3.pop()
print(mi_lista3)
mi_lista3.pop(0)
print(mi_lista3)
#Guardar el elemento que elimino en una variable
eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(eliminado)
#Ordenar listas
lista = ["g", "o", "b", "m", "c"]
lista.sort()
print(lista)
nueva_lista = lista.sort() #El método sort ordena pero no devuelve nada
print(nueva_lista)
print(type(nueva_lista))
lista.reverse()
print(lista)

'''
Práctica Listas 1
Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
'''
mi_lista = ["hola", "adios", 3.14, 55, 33]

'''
Práctica Listas 2
Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.
'''
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

'''
Práctica Listas 3
Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una 
variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
manzana
banana
mango
cereza
sandía
'''
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)