##Varialbes
v_mouse= int(0)
v_teclado=int(0)
v_pendrive=int(0)


total_ventas= int(0)


prom_venMouse=int(0)
Menven_tec=int(0)


##Algoritmo
print("inicio")

print("\n Bienbenido a tu compra de producto!! \n \n ingrese el precio de los sig. Productos: ")

Pmouse = int(input("Mouse: $"))
Pteclado= int(input("Teclado: $"))
Ppendrive =  int(input("Pendrive: $"))

produc= str(input("\n ingrese el producto que quiere comprar: \n \n Mouse = m \n Teclado = t \n Pendrive = p \n o para salir, Fin = f \n ::"))
produc= produc.lower()



if produc == "f":
    print("Se a terminado el programa")    
elif produc == "m" or produc =="t" or produc =="p":
    
    while produc == "m" or produc =="t" or produc =="p":
        cantidad = int(input("ingrese la cantidad del prodructo: "))
        total_ventas += 1        

        if produc == "m":
                v_mouse += 1
                cantT_M =+ cantidad 
                
        elif produc == "t":
                v_teclado += 1
                                
                if cantidad < Menven_tec or cantidad != 0:
                    Menven_tec = cantidad
                ##fin if
                    
        elif produc == "p":
                v_pendrive += 1
        ##fin if
                      

        produc=str(input("\n ingrese el sig. producto  \n\n m - t - p , o, f = para finalizar: "))

        if produc == "f":
                    print("\n Se a terminado el programa")
        else:
                while produc != "m" and produc !="t" and produc !="p" and produc !="f":
                    produc =str(input("ingrese un producto Valido"))
                    produc= produc.lower()
                    if produc == "f":
                        print("\n Se a terminado el programa")
                    ##fin if
                ##fin while
        ##fin if 

    ##fin while
                        
    prom_venMouse = cantT_M / total_ventas

    print("\n Usted tiene un total de: ", total_ventas, "ventas")

    print("\n El Promedio de ventas en Mouse es de: ", prom_venMouse, "unidades por cada venta realizada")

    print("\n La menor venta de Teclados regisrtrada es de: ", Menven_tec, "unidades")


else:
    print("\n \n Usted no a elegido una opcion correcta, reinicie el programa")

##fin if
