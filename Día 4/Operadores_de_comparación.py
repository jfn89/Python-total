#Asignar valor uso =
mi_variable="Hola mundo"
print(mi_variable)
#Comparación uso ==
mi_bool = 10==25
print(mi_bool)
mi_bool = 10==10
print(mi_bool)
mi_bool = 5+5==18-8
print(mi_bool)
mi_bool = "blanco"=="negro"
print(mi_bool)
mi_bool = "blanco"=="blanco" #La comparación es sencible a las mayusculas, si no es exactamente igual va a dar falso
print(mi_bool)
mi_bool = "100"==100 #Aunque ambos son 100 da falso porque uno es str
print(mi_bool)
mi_bool = 100.0==100 #Si los valores son exactamente iguales da verdadero
print(mi_bool)
#Diferencia
mi_bool = 100!=100
print(mi_bool)
mi_bool = 100!=99
print(mi_bool)
#Mayor
mi_bool = 100>99
print(mi_bool)
#Menor
mi_bool = 100<99
print(mi_bool)
#Mayor o igual
mi_bool = 5>=6
print(mi_bool)
#Menor o igual
mi_bool = 5<=6
print(mi_bool)

'''
Práctica Operadores de Comparación 1
Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. Verifica si num1 es mayor o igual que num2 
y almacena el resultado de dicha comparación en una variable llamada mi_bool
'''
num1 = 36
num2 = 17
mi_bool = num1 >= num2

'''
Práctica Operadores de Comparación 2
Crea dos variables (num1 y  num2):
Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
Dentro de num2, almacena el número 5.
Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
'''
num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2

'''
Práctica Operadores de Comparación 3
Crea dos variables (num1 y  num2):
Dentro de num1, almacena el resultado de la operación 64 x 3
Dentro de num2, almacena el resultado de la operación 24 x 8
Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
'''
num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2