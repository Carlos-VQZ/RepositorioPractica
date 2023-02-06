""" Programa1
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 05/02/2023
    Descripcion:Escribir un programa que pregunte al usuario su edad y muestre por pantalla si 
    es mayor de edad o no."""

edad = int(input("Ingrese tu edad: "))  #  Funcion input para introducir datos y casteo int parar 
if edad>=18:  #  Se utiliza la funcion if para establecer una condición 
    print("Eres mayor de edad ")  #  En caso de que la condicion sea verdadera se utiliza la función print para imprimir un mensaje
else:  #  Si la condición es falsa se ejecuta la funcion else
    print("Eres menor de edad ")    #   Si la condición es falsa se ejecutara la funcion print con otro mesaje