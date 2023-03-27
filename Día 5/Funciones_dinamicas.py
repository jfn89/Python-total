def chequear_3_cifras(numero):
    return numero in range (100,1000)

def chequear_3_cifras2(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass

def chequear_3_cifras3(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

def chequear_3_cifras4(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras(658)
print(resultado)
resultado = chequear_3_cifras(65)
print(resultado)

suma = 586 + 402
resultado = chequear_3_cifras(suma)
print(resultado)

resultado = chequear_3_cifras2([55,99,6000])
print(resultado)
print(type(resultado))

resultado = chequear_3_cifras2([555,99,6000])
print(resultado)
print(type(resultado))

resultado = chequear_3_cifras2([55,99,600])
print(resultado)
print(type(resultado))

resultado = chequear_3_cifras3([55,99,60])
print(resultado)
print(type(resultado))

resultado = chequear_3_cifras4([555,99,600])
print(resultado)
print(type(resultado))

'''
Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores 
de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con 
valores positivos y negativos.
No invoques la función, solo es necesario definirla.
'''
def todos_positivos (lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True
lista_numeros = [100, -20, 300]

'''
Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y 
cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
'''
def suma_menores(lista):

    lista_numeros = []

    for n in lista:
        if n in range(0, 1000):
            lista_numeros.append(n)
        else:
            pass
    return sum(lista_numeros)

lista_numeros = [500, 100, 700]

'''
Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y 
devuelva el resultado de dicha cuenta.
'''
def cantidad_pares(lista):
    lista_numeros = []
    for n in lista:
        if n % 2 == 0:
            lista_numeros.append(n)
        else:
            pass
    return len(lista_numeros)
lista_numeros=[1, 50, 502, 755, 34]