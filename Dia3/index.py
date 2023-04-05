#En este archivo se va a explicar el metodo index()

#Con [] nos devuelve el caracter que se encuentre en la posicion pasada como parametro
miTexto = "Esta es una prueba"
resultado = miTexto[9]
print(resultado)
resultado = miTexto[-4] #Indice reverso, empieza por cero y luego desde la derecha por -1
print(resultado)

#Metodo index(), indica la posicion en la que se encuentra un caracter especificado por parametro
resultado = miTexto.index("a")
print(resultado)
resultado = miTexto.index("prueba")
print(resultado)

#Se le puede especificar desde que posicion debe de buscar, no tiene en cuenta la posicion que se le pasa
resultado = miTexto.index("a",5)
print(resultado)

#Tambien se le puede indicar hasta que posicion debe de buscar, no tiene en cuenta la posicion que se le pasa
resultado = miTexto.index("a",5,11) #Dara error debido a que no existe ningun caracter
print(resultado)

#Existe el metodo index pero al reves, rindex()
resultado = miTexto.rindex("a")
print(resultado)