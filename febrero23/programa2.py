""" Programa2
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 06/02/2023
    Descripcion:Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.."""

cadena = "getshulked123"  #  Se declara la contraseña asignandole una string
contraseña = input("Introduce la contraseña: ")  #  con la funcion input se pide al usuario que ingrese la contraseña
if cadena == contraseña.lower():  #  condición if, si cadena es igual a cotraseña se ejecuta, la fucnion lower convierte una cadena de caracteres a minúsculas.
    print("La contaseña coincide")  #  Si la condicion if es verdadera seejecuta
else:  #  fucnion else si la condicion es falsa
    print("La contraseña no coincide")  #  Se ejecuta si la funcion else es verdadera 