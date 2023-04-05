#En este archivo se van a explicar las listas

#Se pueden introducir distintos tipos de datos en una lista
miLista = ["a", "b", "c"]
otraLista = ["hola",55,6.1]
print(type(miLista))
print(len(miLista))

#Se pueden concatenar listas
listaFinal = miLista + otraLista
print(listaFinal)

#Se pueden imprimir los elementos de una lista indicando la posiciones de inicio y fin
resultado = miLista[0:3]
print(resultado)

#Se pueden modificar listas
miLista[0] = "alfa"
print(miLista)

#Se pueden añadir elementos a una lista con append()
miLista.append("beta")
print(miLista)

#Se pueden eliminar elementos dentro de una lista con pop(), por defecto elimina el ultimo elemento de la lista
miLista.pop()
print(miLista)
miLista.pop(0)
print(miLista)
#Tambien se puede almacenar en una variable el elemento eliminado
eliminado = miLista.pop(0)
print(eliminado)

#Para ordenar una lista de forma alfabetica, se emplea sort()
listaFinal = ["h","o","l","a"]
listaFinal.sort()#NO se puede guardar en una variable, modifica la existente
print(listaFinal)

#Se puede invertir el orden de los elementos de una lista con reverse()
listaFinal.reverse()#NO se puede guardar en una variable, modifica la existente
print(listaFinal)
