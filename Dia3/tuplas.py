#En este archivo ese van a explicar las tuplas

#Declaracion de una tupla, puede contener todo tipo de datos NO SE PUEDE MODIFICAR UN ELEMENTO DE UNA TUPLA
miTupla = (1,2,3,4)
print(type(miTupla))
tupla = (5,5.6,"Hola")

print(miTupla[0])
print(miTupla[-2])

#Se puede añadir un tupla dentro de otra tupla
tuplaDoble = (1,2,(10,20),4)
print(tuplaDoble[2][0])

#Se puede transformar una tupla a lista
tuplaDoble = list(tuplaDoble)
print(type(tuplaDoble))
tuplaDoble = tuple(tuplaDoble)
print(type(tuplaDoble))

#Se puede asignar el valor de una tupla a una variable
tupla1 = (1,2,3)
x,y,z = tupla1#Debe de haber el mismo numero de variables que elementos tenga la tupla
print(x,y,z)

#Se puede obtener la longitud de una tupla con len()
print(len(tupla1))

#Se puede contar las veces que aparece un elemento dentro de una tupla con count()
tuplita = (1,1,1,3,4,3,4,2)
print(tuplita.count(1))

#Se puede obtener la posicion en la que se encuentra un elemento con index()
print(tuplita.index(2))