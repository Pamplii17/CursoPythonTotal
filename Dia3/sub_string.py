#En este archivo se van a explicar las extracciones de sub-strings

#Devuelve el caracter de la posicion especificada
texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = texto[2]
print(fragmento)

#Se devuelven los caracteres especificados [desde:hasta(excluido)]
texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = texto[2:5]
print(fragmento)

#Se puede seleccionar solo hasta donde va
texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = texto[:5]
print(fragmento)

#Se puede seleccionar saltos con un tercer parametro
texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = texto[2:10:2]
print(fragmento)
fragmento = texto[::-2]#Saltos de dos desde el final
print(fragmento)