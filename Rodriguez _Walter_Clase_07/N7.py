##Variables

infan= int(0)
joven=int(0)
adult=int(0)
veteran= int (0)

T_compe=int(0)
Tiempo=int(0)
TiempoProm=int(0)

##Algoritmo

print("inicio")

Competidor = str(input("ingrese la categoria del competidor: \n infantil = i \n Joven = j \n Adulto = a \n Veterano = v \n o para salir, Fin = f \n ::"))
Competidor = Competidor.lower()

if Competidor == "f":
    print("se a terminado el programa")
    
elif Competidor == "i" or Competidor=="j" or Competidor == "a"  or Competidor == "v":
    
    while Competidor == "i" or Competidor=="j" or Competidor == "a" or Competidor=="v" :
        
            T_compe += 1
            if Competidor == "i":
                infan += 1
            elif Competidor == "j":
                joven += 1
            elif Competidor == "a":
                adult += 1
            elif Competidor == "v":
                veteran += 1
            Tiempo=int(input("\n ingrese el Tiempo en minutos del competidor: "))
            Competidor=str(input("\n ingrese la categoria del sig. competidor \n\n i - j - a , v , o, f = para finalizar: "))
            ##fin if
            if Competidor == "f":
                    print("se a terminado el programa")
            else:
                while Competidor != "i" and Competidor!="j" and Competidor!="a" and Competidor != "v" and Competidor !="f" :
                    Competidor =str(input("ingrese una categoria Valida"))
                    if Competidor == "f":
                        print("se a terminado el programa")
                    ##fin if
                ##fin while
            ##fin if
           
            TiempoProm += Tiempo
    ##fin while
    TiempoProm = TiempoProm / T_compe
    print("Usted tiene un Total de: ", infan, " infantales compitiendo")
    print("Usted tiene un Total de: ", joven, "  jovenes compitiendo")
    print("Usted tiene un Total de: ", adult, " adultos compitiendo")
    print("Usted tiene un Total de: ", veteran, " veteranos compitiendo")

    print("el Tiempo promedio de los Competidores es de: ", TiempoProm, "minutos")
    print("Usted tiene un total de: ", T_compe, "Competidores")
    
else:
    print("usted no a elegido una opcion correcta")

##fin if

print("FIN")
