##Varialbes
azul= int(0)
rojo=int(0)
verde=int(0)

T_compe=int(0)

tiempoMin=int(999)
##Algoritmo
print("inicio")

equipo= str(input("ingrese el color del competidor: \n azul = a \n Rojo = r \n Verde = v \n o para salir, Fin = f \n ::"))
equipo= equipo.lower()

if equipo == "f":
    print("Se a terminado el programa")    
elif equipo == "a" or equipo =="r" or equipo =="v":
    
    while equipo == "a" or equipo =="r" or equipo =="v":
        
            T_compe += 1                        
            if equipo == "a":
                azul += 1
            elif equipo == "r":
                rojo += 1
            elif equipo == "v":
                verde += 1
            ##fin if
            tiempo= int(input("ingrese el tiempo en min del competidor: "))
            if tiempo < tiempoMin:
                tiempoMin = tiempo
            ##fin if

            equipo=str(input("\n ingrese el equipo del sig. competidor  \n\n a - r - v , o, f = para finalizar: "))

            if equipo == "f":
                    print("\n Se a terminado el programa")
            else:
                while equipo != "a" and equipo !="r" and equipo !="v" and equipo !="f":
                    equipo =str(input("ingrese una seccion Valida"))
                    if equipo == "f":
                        print("\n Se a terminado el programa")
                    ##fin if
                ##fin while
            ##fin if 


    ##fin while
    compe_A_V = azul + verde
    print("\n Usted tiene un total de: ", compe_A_V, "de competidores en el equipo Azul y Verde")

    print("\n Usted tiene un total de: ", T_compe, "competidores")

    print("\n El mejor Tiempo Minimo registrado es de: ", tiempoMin, "minutos")


else:
    print("\n \n Usted no a elegido una opcion correcta")

##fin if


print("FIN")
          
