##5. Ingresar una serie de importes de compra,
##calcular y mostrar en cada ciclo el importe más el IVA del %21.

##Finalizar la entrada de datos con el valor cero.

print("inicio")

compra= int(input("ingrese su compra: $"))

while compra > 0:
    
    compraT= compra + (compra * 0.21)
    print("su precio final mas el 21% iva es de: $", compraT)
    
    compra=int( input("\n \n ingrese nuevamente una compra o 0 para finalizar: $"))
#fin while

print("\n Gracias!!,  vuelva pronto")
print("\n FIN")
