#2.
#Ingresar en el saldo de una caja de ahorros,el importe a retirar.
#Si tiene saldo suficiente, mostrar el nuevo saldo en cuenta.
#En caso contrario, mostrar el mensaje “No es posible retirar esa cantidad de dinero”.

print("Inicio")

#Variables

cajaAhor= float(input("Ingrese el monto de la caja de ahorros: "))

retiro= float(input("Ingrese el monto a retirar: "))


#Algoritmo

if retiro <= cajaAhor:
    cajaAhor= cajaAhor - retiro
    print("Su saldo restante en la caja de ahorros es de: $", cajaAhor)

else:
    print("No es posible retirar esa cantidad de dinero")
#fin If

    
print("FIN")
