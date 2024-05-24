##(8)
print("Alumno Regular")

print("INICIO")

##VAR

asis=int(input("ingre la cantidad de Asistencias del alumno:  "))

inasis=int(input("Ingrese la cantidad de Inasistencias del alumno:  "))

##Algoritmo

Tclass= asis + inasis

print("se dictaron:  ", Tclass, "clases")

PorAsis= (asis / Tclass) * 100

print(" El porcentaje de asistencias del alumno es de:  ", PorAsis, "%")

print("FIN")
