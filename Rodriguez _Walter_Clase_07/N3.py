#N3- Ingresar 10 letras, una a una y mostrar la cantidad de vocales.

print("Inicio")

palabra= str(" ")
vocales=int(0)

for i in range (10):
    
    letra= str ( input("ingrese una letra: "))
    letra= letra.lower()
    if letra == "a" or letra== "e" or letra=="i" or letra=="o" or letra=="u":
        vocales+=  1
    #fin if
        
    if letra == " ":
        palabra=  palabra + " "
    else:
            palabra = palabra + letra
    #fin if

#fin for
print("El la palabra: ", palabra, "contiene: ",vocales, "vocales")
