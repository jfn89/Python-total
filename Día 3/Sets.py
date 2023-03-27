mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)
mi_set = set([1,2,3,4,5,1,1,1,2,2,2])
print(type(mi_set))
print(mi_set)
mi_set = set([1,2,3,4,(1,2,3),1,1,1,2,2,2])
print(type(mi_set))
print(mi_set)
mi_set = set([1,2,3,4,5])
print(len(mi_set))
print(2 in mi_set)
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s1 = {1,2,3}
s1.add(4)
print(s1)
s1 = {1,2,3}
s1.add(2)
print(s1)
s1 = {1,2,3}
s1.remove(3) #Si quiero remover un elemento que no tiene da error
print(s1)
s1 = {1,2,3}
s1.discard(6) #No da error si el elemento a descartar no esta en el set
print(s1)
s1 = {1,2,3}
s1.pop() #Elimina elemento aleatorio
print(s1)
s1 = {1,2,3}
sorteo = s1.pop()
print(sorteo)
s1 = {1,2,3}
s1.clear() #Vacia el set
print(s1)

'''
Práctica Sets 1
Une los siguientes sets en uno solo, llamado mi_set_3:
{1, 2, "tres", "cuatro"}
{"tres", 4, 5}
'''
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

'''
Práctica Sets 2
Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
'''
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.pop())

'''
Práctica Sets 3
Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
'''
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")