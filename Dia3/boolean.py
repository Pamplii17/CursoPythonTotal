#En este archivo se van a explicar los tipos de datos boolean

#Declaracion de un booleano
verdad = True
falso = False
print(type(verdad))
print(verdad)

#Otras formas de obtener booleanos
numero = 5 > 2+3
print(type(numero))
print(numero)
numero1 = 5 == 2+3
print(numero1)
numero2 = 5 != 2+3
print(numero2)
numero3 = 5 >= 2+3
print(numero3)
numero4 = bool(5<6)
print(numero4)

#Se puede añadir a una lista
lista = [1,2,3,4]
control = 5 in lista
print(control)