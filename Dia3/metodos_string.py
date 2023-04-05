#En este archivo se van a explicar los metodos STRING

#Pasar todos los caracteres de una variable tipo str a mayusculas: upper()
texto = "Este es el texto de Javier"
resultado = texto.upper()
print(resultado)
resultado = texto[2].upper()
print(resultado)

#Pasar todos los caracteres de una variable tipo str a minusculas: lower()
resultado = texto.lower()
print(resultado)

#El metodo split() permite separar el string en elementos para guardarlos en una lista, por defecto divide por espacios
resultado = texto.split()
print(resultado)
resultado = texto.split("t")#Toma como separador el caracter t
print(resultado)

#El metodo join() permite unir elementos, y los separa por elemento que se le indique: " ".join(), en este caso por espacios
texto1 = "Aprender"
texto2 = "Python"
texto3 = "es"
texto4 = "genial"
resultado = "-".join([texto1,texto2,texto3,texto4])
print(resultado)

#El metodo find() permite buscar caracteres en un string, la diferencia con index, es que si no existe el elemento indicado devuelve un -1
resultado = texto.find("z")
print(resultado)

#El metodo replace() permite remplazar un string por otro
resultado = texto.replace("Javier", "Sergi")
print(resultado)