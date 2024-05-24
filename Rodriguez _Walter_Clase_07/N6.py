##6. En una fabrica que cuenta con tres Áreas: Armado, Empaquetado y Ventas.  (a – e – v )
##Se necesita saber:
##El total de empleados de cada área. 
##El total general de empleados.
##El sueldo promedio de los empleados.

##Los datos a ingresar por cada empleado son: Área y Sueldo.	

##Nota: finalizar el programa cuando se ingrese la palabra “fin” al momento de solicitar el Área.

##Variables

emple_a= int(0)
emple_e=int(0)
emple_v=int(0)

T_emple=int(0)
sueldo=int(0)
suelProm=int(0)

##Algoritmo

print("inicio")

area= str(input("ingrese el area del empleado: \n Armado= a \n Empaquetado= e \n Ventas= v \n o para salir, Fin = f \n ::"))
area= area.lower()

if area == "f":
    print("se ah terminado el programa")
    
elif area == "a" or area=="e" or area=="v":
    
    while area == "a" or area=="e" or area=="v" :
        
            T_emple += 1
            if area == "a":
                emple_a += 1
            elif area == "e":
                emple_e += 1
            elif area == "v":
                emple_v += 1
            sueldo=int(input("\n ingrese el sueldo del empleado: $"))
            area=str(input("\n ingrese el Area del siguiente empleado \n\n a - e - v , o, f = para finalizar: "))
            if area == "f":
                    print("se ah terminado el programa")
            else:
                while area != "a" and area!="e" and area!="v" and area!="f" :
                    area=str(input("ingrese un Area Valida"))
                    if area == "f":
                        print("se ah terminado el programa")
                    ##fin if
                ##fin while
            ##fin if 
            suelProm += sueldo
    ##fin while
    suelProm = suelProm / T_emple
    print("Usted tiene un Total de: ", emple_a, " en el Area de Armado")
    print("Usted tiene un Total de: ", emple_e, " en el Area de Empaquetado")
    print("Usted tiene un Total de: ", emple_v, " en el Area de Ventas")
    print("el sueldo promedio de los empleados es de: $", round(suelProm,2))
    print("Usted tiene un total de: ", T_emple, "empleados")
    
else:
    print("usted no a elegido una opcion correcta")

##fin if

print("FIN")





