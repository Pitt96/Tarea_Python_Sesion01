pN=1.5
pA=3
pU=2
print("*******************************************")
cantN=int(input("Ingrese la cantidad de boletos para niños: \n>"))
cantA=int(input("Ingrese la cantidad de boletos para adultos: \n>"))
cantU=int(input("Ingrese la cantidad de boletos para universitarios: \n>"))
precioGasolina=int(input("Digite el monto del combustible:\nS/."))

precioF=cantN*pN+cantA*pA+cantU*pU
ganancia=precioF-precioGasolina

print("*****************************************")
print(f"Total cobrado:  S/.{precioF}")
print(f"La ganancia es: S/.{ganancia}")
