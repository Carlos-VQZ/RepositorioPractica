""" Programa3
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 08/02/2023
    Descripcion:Escribir un programa que pregunte nombre del usuario en la consola y un número entero e imprima por pantalla en líneas  distintas el nombre del usuario tantas veces como el número     introducido..."""

nombre = input("¿Cual es tu nombre? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))