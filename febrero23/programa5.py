""" Programa5
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 11/02/2023
    Descripcion:Calculadora de indice de masa corporal...."""

peso = float(input("Escribe la peso en kilogramos: "))  #  funcion imput para introducir y casteo para introducir datos 
altura = float(input("Escribe la altura en metros: "))  #  funcion imput para introducir y casteo para introducir datos 
imc = peso//altura**2  #  Se declara variable imc en la cual se realiza una división con el operador barra doble y una ótencia con el perador asterisco doble

if imc >=0 and imc <= 18.5:  #  con la fucion if se realiza una doble condición con el operador boleano and
 print("imc: ",imc,"Underweight")  #  Si la condicion if es verdera se ejecuta la funcion print
elif imc >=18.6 and imc <= 24.9:  #  con la fucion if se realiza una doble condición con el operador boleano and
 print("imc: ",imc,"Normal")  #  Si la condicion anterior es falsa y esta condición elif es verdera se ejecuta la funcion print
elif imc >= 25 and imc <= 29.9:  #  con la fucion if se realiza una doble condición con el operador boleano and
 print("imc: ",imc,"Overweight")  #  Si la condicion elif  anterior es falsa y esta condición elif es verdadera se ejecuta la funcion print
else:  #  Si todas las condciones anteriores son falsas se ejecuta la fucnion else 
 print ("imc: ",imc, "Obesity")  #  Se ejecuta cuando la funcion else es verdadera

    
     