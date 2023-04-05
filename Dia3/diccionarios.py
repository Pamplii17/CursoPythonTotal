#En este archivo se van a explicar los diccionarios

#Declaracion de un diccionario
dic = {"c1":"valor1", "c2":"valor2","c3":"valor3"}#Las claves deben de ser unicas
print(type(dic))
print(dic)

#Se puede imprimir lo que contiene una clave con:
resultado = dic["c1"]
print(resultado)

#Se pueden declarar todo tipos de datos en un diccionario
cliente = {"nombre":"Juan","apellido":"Fuentes","peso":88,"talla":1.78}
consulta = cliente["apellido"]
print(consulta)

#Se pueden incluir dentro de un diccionario listas o diccionarios entre otros
dic1 = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":300}}
print(dic1["c2"][0])
print(dic1["c3"]["s2"])

#Se pueden aplicar metodos aprendidos como el siguiente
dic2 = {"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic2["c2"][1].upper())

#Se puede añadir contenido a un diccionario de la siguiente forma:
dic3 = {1:"a",2:"b"}
print(dic3)
dic3[3] = "c"
print(dic3)

#Se puede modificar el contenido de un diccionario de la siguiente forma:
dic3[2] = "B"
print(dic3)

#Se pueden imprimer el nombre de las claves con keys()
print(dic3.keys())

#Se pueden imprimir los valoes de las claves con values()
print(dic3.values())

#Para imprimir todo lo que hay en un diccionario se emplea items()
print(dic3.items())