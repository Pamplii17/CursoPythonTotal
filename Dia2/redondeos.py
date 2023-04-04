#En este archivo se van a explicar los redondeos

#Ejemplo de round sin parametros
print(90/7)
print(round(90/7))#Si no se le pasa ningun parametro, por defecto redondea a cero decimales
resultado = round(90/7)
print(resultado)

#Ejemplo de round con parametros, el segundo parametro es para indicar cuantos decimales queremos que se redondeen
valor = round(95.6666666666,2)
print(valor)
valor = round(valor)
print(type(valor))

#Otro ejemplo
valor2 = 95.6666666666666666
print(round(valor2))
print(type(valor2))