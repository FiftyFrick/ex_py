# 10. Ingresar una temperatura y mostrar los siguientes mensajes según corresponda:

# negativo “bajo cero”
# entre 0 y 15  “fresco”
# 16 y 20  “templado”
# 21 y 45  “caluroso”

temp=float(input("Ingrese la temperatura: "))

if temp < 0:
    print("Bajo Cero")

elif temp == 0 or temp <= 15 :
     print("Fresco")

elif temp == 16 or temp <= 20 :
    print("Templado")

elif temp == 21 or temp <= 45 :
    print("Caluroso")

else:
    print("Temperatura Fuera de Rango")

#fin If
    
print("FIN")
    
