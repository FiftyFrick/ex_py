#9. Ingresar un valor y la moneda, si es dólar multiplicar el valor por 40.23 y si es euro por 45.44.

print("Inicio")

#Variables

valor=float(input("ingrese su Valor: $"))

moneda=int(input(" Ingrese 1 = Dolar \n Ingrese 2 = Euro \n"))

#Algoritmo

if moneda == 1:
    valor= valor * 40.23
    print("su valor en Dolar es de: $",valor)
elif moneda == 2:
    valor= valor * 45.44
    print("su valor en Euro es de: $",valor)

else:
    print("usted no a elegido una moneda")

#fin If 

print("FIN")


