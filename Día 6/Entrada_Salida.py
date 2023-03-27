mi_archivo = open("Prueba.txt")
#print(mi_archivo.read())
#print(mi_archivo.readline())
'''
Lee e imprime una vez, si lo hago de a una linea va dejando como en un punto y
empieza desde la siguiente despues.
'''
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()