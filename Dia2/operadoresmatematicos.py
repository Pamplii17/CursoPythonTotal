#En este archivo se van a explicar los operadores matematicos

#Realizacion de operaciones matematicas empleando el formateo de cadenas
x = 6
y = 2
print(f"{x} mas {2} es igual a {x+y}")
print(f"{x} menos {2} es igual a {x-y}")
print(f"{x} por {2} es igual a {x*y}")
print(f"{x} entre {2} es igual a {x/y}")

#Otro tipo de division es: la division en al que nos quedamos con el valor entero
z = 7
print(f"{z} entre(int) {2} es igual a {z//y}")

#Otro tipo de division es: la que devuelve el resto de la division
print(f"{z} entre(resto) {2} es igual a {z%y}")

#Tambien se pueden hacer operaciones con exponentes
print(f"{x} elevado {2} es igual a {x**y}")
print(f"{x} elevado {2} es igual a {x**3}")

#Por ultimo, se pueden hacer raices cuadradas
print(f"La raiz cuadrada de {x} es {x**0.5}")
