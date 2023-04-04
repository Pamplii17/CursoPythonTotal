#En este archivo se van a explicar los tipos de variables INT y FLOAT

#Se declara una variable con valor un numero NOTA: con la funcion type() se imprime el tipo del valor
miNumero = 1
print(miNumero)
print(type(miNumero))

#Se puede declarar una variable que sea una operacion
operacion = 1 + 3
print(operacion)
print(operacion+operacion)

#Se puede declarar un numero tipo decimal
miDecimal = 5.8
print(miDecimal)
print(type(miDecimal))
operacion2 = miNumero+miDecimal
print(operacion2)
print(type(operacion2))

#Se puede concatenar String con Int en print NOTA: input pasa todo lo que se le ingresa a STRING
edad = input("Ingresa tu edad: ")
print("Tu edad es: " + edad)
#nuevaEdad = edad + 1
#print("Vas a cumplir: " + nuevaEdad + " el año que viene")
print(type(edad))
print(edad + edad)