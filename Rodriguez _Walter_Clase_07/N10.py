##Varialbes
corrientes= int(0)
chaco=int(0)
misiones=int(0)

venCorr=int(0)

sueldoMax=int(0)
##Algoritmo
print("inicio")

sucur= str(input("ingrese la sucursal del empleado: \n Corrientes = co \n Chaco = ch \n Misiones = mi \n o para salir, Fin = f \n ::"))
sucur= sucur.lower()

if sucur == "f":
    print("Se a terminado el programa")    
elif sucur == "co" or sucur =="ch" or sucur =="mi":
    
    while sucur == "co" or sucur =="ch" or sucur =="mi":
                                            
            if sucur == "co":
                corrientes += 1
            elif sucur == "ch":
                chaco += 1
            elif sucur == "mi":
                misiones += 1
            ##fin if
                
            cargo= str(input("ingrese el cargo del empleado: vendedor, administrador, encargado, o cajero : "))
            cargo = cargo.lower()
            if cargo == "vendedor" and sucur == "co":
                            venCorr += 1
            ##fin if

            sueldo = int(input("ingrese el Sueldo del empleado: $"))
            if sueldo > sueldoMax:
                sueldoMax = sueldo
            ##fin if

            sucur=str(input("\n ingrese la sucursal del sig. empleado  \n\n co - ch - mi , o, f = para finalizar: "))
            if sucur == "f":
                    print("\n Se a terminado el programa")
            else:
                while sucur != "co" and sucur !="ch" and sucur !="mi" and sucur !="f":
                    sucur =str(input("ingrese una seccion Valida"))
                    sucur= sucur.lower()
                    if sucur == "f":
                        print("\n Se a terminado el programa")
                    ##fin if
                ##fin while
            ##fin if 

    ##fin while
    emple_C_M = corrientes + misiones

    print("\n Usted tiene un total de: ", emple_C_M, "empleados entre Corrientes y Misiones")

    print("El Total de vendedores en Corrientes es de: ", venCorr)

    print("\n El Sueldo Maximo registrado de un empleado es de: $", sueldoMax)


else:
    print("\n \n Usted no a elegido una opcion correcta")

##fin if

