#Proyecto del Dia2
#Autor: Javier Pampliega Garcia
#Version: 1.0

#Problema: Se debe de calcular una calculadora de comisiones

nombre = input("Dime tu nombre: ")
ingreso = input("¿Cuanto has generado?")
print(f"El empleado: {nombre} ha generado {ingreso}€, por lo tanto, le corresponde {round((int)(ingreso)*0.13,2)}€ de comision")