#En este archivo se van a explicar las variables

#Se declara una variable nombre y se imprime
nombre = "Javier"
print(nombre)

#Se asigna otro valor a la variable nombre
nombre = "David"
print(nombre)

#Se puede declarar una variable con un contenido numerico, ademas de poder sumar variables
edad = 30
edad2 = 15
print(edad)
print(edad+edad2)

#Se puede igualar un input a una variable, por lo tanto, lo que el usuario introduzca por pantalla se guardara en la variable
nombre = input("Dime tu nombre: ")
print(nombre)

#Se pueden concatenar variables NOTA: no se puede concatenar un tipo string con un int o viceversa
nombre = "Hola "
nombre2 = "Javier"
frase = nombre + nombre2
print(frase)