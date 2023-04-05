#Proyecto del Dia3
#Autor: Javier Pampliega Garcia
#Version: 1.0

#Problema: Se debe de crear un analizador de texto. Este solicitara un texto al usuario y realizar cinco funciones distintas.

texto = input("Introduce el texto que deseas analizar: ")   #Se recoge la entrada del usuario

letras = input("Introduce las letras separadas por comas: ")    #Se recoge la entrada del usuario
letras = letras.split(",")  #Se transforma el STRING, el cual ha sido dividido por espacios
print(f"Frase introducida: {texto}")
print(f"Letras seleccionadas: {letras[0]},{letras[1]} y {letras[2]}")   #Se imprimen los valores introducidos por el usuario

print(f"La letra {letras[0]} aparece {texto.count(letras[0])} veces")   #Se comprueba cuantas veces aparece cada letra en la lista
print(f"La letra {letras[1]} aparece {texto.count(letras[1])} veces")
print(f"La letra {letras[2]} aparece {texto.count(letras[2])} veces")

longitudTexto = len(texto.split(" "))   #Se cuenta el numero de palabras en funcion del STRING divididO por espacios
print(f"El texto tiene {longitudTexto} palabras")   #Se imprimer el valor obtenido

print(f"La primera letra del texto es: {texto[:1]} y la ultima: {texto[-1]}")   #Se emplea indexacion para buscar el primer caracter y el ultimo
estaEnTexto = "Python" in texto     #Se devuelve un booleano en funcion de si esta o no la palabra en el texto
dic = {True: "Esta la palabra Python en el texto introducido",False:"No esta la palabra Python en el texto introducido"}    #Se crea un diccionario con claves booleanas
print(dic[estaEnTexto])     #Se devuelve el valor de la clave en funcion del tipo de bool obtenido