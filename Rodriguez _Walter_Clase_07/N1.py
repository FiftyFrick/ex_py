print("Inicio")

promT=int(0)
dia=int (0)

for i in range (7):

    dia = 1 + dia 
    print("Dia Nº: ", dia)
    Tempdia=int(input("Escriba la temperatura del dia:" ))

    promT = (promT + Tempdia)
#fin for i
    
promT = promT / 7

print("el promedio de la semana es: ", round (promT,2))

print("FIN")
