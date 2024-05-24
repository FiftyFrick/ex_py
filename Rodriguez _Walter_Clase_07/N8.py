compra= int(0)
venta=int(0)
publicidad=int(0)

T_emple=int(0)
mayores=int(0)
sueldo=int(0)
suelProm=int(0)

##Algoritmo

print("inicio")

secc= str(input("ingrese la seccion del empleado: \n Compra = c \n Ventas= v \n Publicidad = p \n o para salir, Fin = f \n ::"))
secc= secc.lower()

if secc == "f":
    print("Se a terminado el programa")
    
elif secc == "c" or secc=="v" or secc=="p":
    
    while secc == "c" or secc=="v" or secc=="p":

            T_emple += 1                        
            if secc == "c":
                compra += 1
            elif secc == "v":
                venta += 1
            elif secc == "p":
                publicidad += 1
            edad = int(input("\n Ingrese la EDAD del empleado: "))
            if edad > 50:
                mayores += 1
            ##fin if
                
            sueldo=int(input("\n ingrese el sueldo del empleado: $"))

            secc=str(input("\n ingrese la seccion del siguiente empleado \n\n c - v - p , o, f = para finalizar: "))

            if secc == "f":
                    print("\n Se a terminado el programa")
            else:
                while secc != "c" and secc!="v" and secc!="p" and secc!="f" :
                    secc=str(input("ingrese una seccion Valida"))
                    if secc == "f":
                        print("\n Se a terminado el programa")
                    ##fin if
                ##fin while
            ##fin if 
            suelProm += sueldo
    ##fin while
    suelProm = suelProm / T_emple
    T_com_publi = compra + publicidad

    print("\n Usted tiene un Total de: ", compra, " en el Area de Compras ")
    print("Usted tiene un Total de: ", venta, " en el Area de Ventas")
    print("Usted tiene un Total de: ", publicidad, " en el Area de Publicidad")
    
    print("\n Usted tiene un Total de: ", mayores, "mayores de edad en la empresa")
    print("\n El sueldo promedio de los empleados es de: $", round (suelProm,2))
    
    print("\n Usted tiene un total de: ", T_com_publi, "empleados en la seccion de compra y publicidad")
    
else:
    print("\n \n Usted no a elegido una opcion correcta")

##fin if


print("FIN")

