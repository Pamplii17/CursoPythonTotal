#En este archivo se van a explicar las conversiones

#Suma de int y float
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

#Transformar una variable tipo float a tipo int
num3 = 5.8
print(num3)
print(type(num3))
numInt = int(num3)
print(numInt)
print(type(numInt))

#Transformar uan variable de tipo a INT a FLOAT
num4 = 20
print(num4)
print(type(num4))
num4 = float(num4)
print(type(num4))


#Transformar lo que guarda un input(STRING) a INT
edad = input("Introduce tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nuevaEdad = 1 + edad
#Sale error porque no se pueden concatenar distintos tipos de datos, en este caso, un STRING con un INT
#print("Tu nueva edad va a ser: " + nuevaEdad)
