print("inicio")

gasto= int(input("ingrese cuanto gasto en el Taxi: "))
gastoT=int(0)

while gasto > 0:
    gastoT += gasto
    gasto=int( input("ingrese nuevamente cuanto gasto en el taxi o 0 para finalizar: "))
#fin while
    
print("Usted gasto en total: ", gastoT)

print("FIN")
