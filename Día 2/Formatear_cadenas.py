x = 10
y = 5
z = x + y
print("Mis números son " + str(x) + " y " + str(y))
print("Mis números son {} y {}".format(x,y))
print("Mis números son {} y {}".format(y,x))
print("La suma de {} y {} es igual a {}".format(y,x,y+x))
print("La suma de {} y {} es igual a {}".format(y,x,z))
color = "rojo"
matricula = 541926
print(f"El auto es {color} y su matrícula es {matricula}")

'''
Práctica Formatear Cadenas 1
Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al 
resultado correcto.
'''
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

'''
Práctica Formatear Cadenas 2
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al 
resultado correcto.
'''
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

'''
Práctica Formatear Cadenas 3
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al 
resultado correcto.
'''
puntos_anteriores = 875
puntos_nuevos = 350
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores+puntos_nuevos} puntos")

