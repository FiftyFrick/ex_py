##Varialbes
vendedor= int(0)
administrativo=int(0)
gerente=int(0)


sueldoProm_gere=int(0)
sueldoMax_admin=int(0)

total_emple= int(0)

##Algoritmo
print("inicio")

cate= str(input("ingrese la categoria del empleado: \n Vendedor = v \n Administrativo = a \n Gerente = g \n o para salir, Fin = f \n ::"))
cate= cate.lower()

if cate == "f":
    print("Se a terminado el programa")    
elif cate == "v" or cate =="a" or cate =="g":
    
    while cate == "v" or cate =="a" or cate =="g":

        total_emple += 1
        
        if cate == "v":
                vendedor += 1
        elif cate == "a":
                administrativo += 1
        elif cate == "g":
                gerente += 1
        ##fin if

        sueldo = int(input("ingrese el Sueldo del empleado: $"))

        if cate == "g":
                sueldoProm_gere += sueldo  
        ##fin if

        if sueldo > sueldoMax_admin and cate == "a":
                sueldoMax_admin = sueldo
        ##fin if
                      

        cate=str(input("\n ingrese la categoria del sig. empleado  \n\n v - a - g , o, f = para finalizar: "))
        if cate == "f":
                    print("\n Se a terminado el programa")
        else:
                while cate != "v" and cate !="a" and cate !="g" and cate !="f":
                    cate =str(input("ingrese una categoria Valida"))
                    cate= cate.lower()
                    if cate == "f":
                        print("\n Se a terminado el programa")
                    ##fin if
                ##fin while
        ##fin if 

    ##fin while
    

    print("\n Usted tiene un total de: ", total_emple, "empleados")
    if sueldoProm_gere > 0:
        sueldoProm_gere = sueldoProm_gere / gerente
        print("\n El Promedio de los sueldos de la categoria Gerente es de: $", sueldoProm_gere)
    else:
        print("\n El Promedio de los sueldos de la categoria Gerente es de: $ 0") 

    print("\n El Sueldo Maximo registrado en la categoria Administrativo es de: $", sueldoMax_admin)


else:
    print("\n \n Usted no a elegido una opcion correcta")

##fin if
