#1. Ingresar dos números y mostrar el mayor de ellos. Si los números ingresados fueran iguales,
#mostrar el mensaje “Los números son iguales”.

print("Inicio")

#Variables

num1= int(input("Ingrese el numero 1: "))
num2= int(input("Ingrese el numero 2: "))

#Algoritmo

if num1 > num2:
    print(" El numero 1 es mayor que el numero 2")

elif num2 > num1:
    print("El numero 2 es mayor que el numero 1")

else:
    print("Los 2 numeros son iguales")

print("FIN")
