texto = input("Por favor ingresá el texto que querés analizar: ")
letra1 = input("Por favor ingresá una letra: ")
letra2 = input("Por favor ingresá otra letra: ")
letra3 = input("Por favor ingresá una letra más: ")
print("\nREPETICION DE LETRAS\n")
cantidad_letra1 = texto.lower().count(letra1.lower())
cantidad_letra2 = texto.lower().count(letra2.lower())
cantidad_letra3 = texto.lower().count(letra3.lower())
print(f"En tu texto la letra \"{letra1}\" aparece {cantidad_letra1} veces, la letra \"{letra2}\" aparece {cantidad_letra2}"
      f" veces y la letra \"{letra3}\" aparece {cantidad_letra3} veces.")
print("\nCANTIDAD DE PALABRAS\n")
texto_lista = texto.split()
texto_lista.reverse()
cantidad_palabras = len(texto_lista)
print(f"El texto que ingresaste tiene {cantidad_palabras} palabras.")
print("\nLETRAS DE INICIO Y FIN")
primer_letra = texto[0]
ultima_letra = texto[-1]
print(f"Tu texto comienza con \"{primer_letra}\" y termina \"{ultima_letra}\"")
print("\nTEXTO INVERTIDO")
texto_alreves = " ".join(texto_lista)
print(f"Tu texto al reves es:\n {texto_alreves}")
print("\nBUSCANDO LA PALABRA PYTHON")
python = {True:"contiene",False:"no contiene"}
llave = "python" in texto.lower()
print(f"Tu texto {python[llave]} la palabra Python.")

