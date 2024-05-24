print("Inicio")

#Variables

Tpagar=float(input("igrese el total a pagar: "))

print("Elija la opcion con la que desea pagar el total")

print("Elija la opcion: `E` para pagar en Efectivo")

print("Elija la opcion: `T` para pagar en Tarjeta")

Opc=input("¿E o T?")

#Algoritmo

if Opc == "E" or Opc == "e":
    print("usted a elegido pagar en Efectivo, usted obtendra un 10% de Descuento")
    Tpagar= Tpagar - (Tpagar * 0.10) 
    print(" El total a pagar es de: ", Tpagar)

elif Opc == "T" or Opc == "t":
    print("usted a elegido pagar en Tarjeta, usted obtendra un 5% de Recargo")
    Tpagar= Tpagar + (Tpagar * 0.5)
    print(" El total a pagar es de: ", Tpagar)

else:
    print("usted NO a elegido una opcion de pago")

#Fin If
    
print("FIN")
