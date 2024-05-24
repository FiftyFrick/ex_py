print("Inicio")

#Variables

edad=int(input("ingrese su edad: "))

naci=int(input(" ingrese 1 si es Argentino/a, si no ingrese 2: "))

#Algoritmo

if naci == 1 and edad >= 18:
    print("Usted puede votar")

else:
    print("Usted no puede votar, no cumple los requisitos")
#Fin If

print("Fin")
    
