#En este archivo se van a explicar los formateos de cadenas

#Se pueden imprimir numeros convirtiendolos a string con str(), aunque no es la mejor opcion
x = 10
y = 5
print("Mis numero son: " + str(x) + str(y))

#Otra forma de hacerlo es con .format()
print("Mis numeros son: {} y {}".format(x,y))
print("La suma de {} y {} es: {}".format(x,y,x+y))

#Otra forma mas es con: 
color = "rojo"
matricula = "134134S"
print(f"El coche es {color} y su matricula es: {matricula}")