print("Inicio")

#Variables

montoT=float(input("ingrese el monto Total de su compra: $"))

print ("\n Nosotros trabajamos unicamente con tarjetas Visa y Mastercad")
tarjeta=int(input("\n ingrese 1 desea usar VISA: \t ingrese 2 si desea usar Mastercad: \n "))

#Algoritmo

if tarjeta == 1:
    print("\t Usted a elegido pagar con Visa \n")

elif tarjeta == 2:
        print("\t Usted a elegido pagar con Mastercad \n")

else:
            print("\t Usted no a elegido un metodo de pago \n")
#fin if
            
if tarjeta == 1 or tarjeta == 2:
    
    cuotas=int(input("\t Ingrese la cantidad de cuotas en la que desea pagar el monto Total: \n"))

    cuota=int

    if cuotas == 12:
        cuota = (montoT / cuotas)
        print("\t Al pagar en 12 cuotas no tendra intereses y las cuotas seran de: $", round(cuota, 2), "\n"  )

    else:
            cuota = (montoT + (montoT * 0.20)) / cuotas
            print("\t Usted recibe un Recargo del 20% en su monto Total, al no pagar en 12 cuotas, \n  su cuota mensual es de: $", round(cuota, 2), "\n")
#fin if

print("\t Fin")
            
            
