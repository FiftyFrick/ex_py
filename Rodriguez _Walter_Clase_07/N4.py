##4. Ingresar una serie de números hasta que el usuario ingrese un cero.
##Al finalizar, indicar la cantidad de números menores a 15.

print("inicio")

numeroS=int(0)
menores=int(0)
numero= int(input("ingrese su numero: "))

while numero > 0:
    numeroS += 1
    if numero < 15:
        menores += 1
        #fin if
    numero=int( input("ingrese nuevamente un numero o 0 para finalizar: "))
#fin while

print("coloco: ", numeroS, "numero y tiene: ", menores, "numeros menores a 15")

print("FIN")
