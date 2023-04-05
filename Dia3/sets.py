#En este archivo se van a explicar los sets

#Declaracion de un set, solo se puede introducir un argumento dentro de un set NO SE PUEDEN MODIFICAR LOS ELEMENTOS ASI COMO LLAMAR A UN INDICE DEL MISMO
set = set([1,2,3,4,5])
print(type(set))
print(set)
otroSet = {1,2,3}#Otra forma de declarar un set
print(type(otroSet))
print(otroSet)

#Por muchos numeros repetidos que se pongan, solo se imprimira uno
setRep = {1,1,2,2,2,2,2,3,3,3,1,1,1,3,4,4,}
print(setRep)

#Se puede introducir una tupla dentro de un set
setTupla = {1,2,3,1,(2,3,4,2,1),2,4,5}
print(setTupla)

#Se puede saber la longitud de un set con len()
print(len(setTupla))

#Se pueden realizar consultas, saber si un elemento dentro de un set
print(2 in setTupla)

#Se pueden unir sets con union()
s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)

#Se pueden agregar elementos a un set con add()
setAdd = {1,2,3}
setAdd.add(4)
print(setAdd)

#Se puede eliminar un elemento de un set con remove()
setRemove = {1,2,3}
setRemove.remove(3)
print(setRemove)

#Metodo discard no da error si no existe el elemento, en caso de que si lo elimina
setDisc = {1,2,3,4,5}
setDisc.discard(6)
print(setDisc)

#pop() elimina un elemento de forma aleatoria
s4 = {1,2,3,4,5,6}
s4.pop()
print(s4)

#Para vaciar un set se emplea clear()
s4.clear()
print(s4)