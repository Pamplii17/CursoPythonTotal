#En este archivo se van a explicar las propiedades de los string

#El string es inmutable, es decir no se puede modificar directamente
nombre = "Carina"
#nombre[0] = "K"
nombre = "Karina"
print(nombre)

#Se pueden concatenar strings
n1 = "Kari"
n2 = "na"
print(n1 + n2)

#Se pueden mutliplicar strings de la siguiente manera
print(nombre*10)

#Se pueden añadir saltos de linea, se añaden tres comillas """ y se presiona ENTER
poema = """Mil pequeños 
peces blancos
estan en el agua"""
print(poema)

#Se puede comprobar la existencia de caracteres de un string, devuelve True o False en funcion de si esta o no
print("agua" in poema)

#Se puede saber la longitud de un string con len()
print(len(poema))