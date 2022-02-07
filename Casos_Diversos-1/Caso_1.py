nombre=input("Ingrese el nombre del trabajador: \n>")
horasT=int(input("Ingrese las horas de trabajo: \n>"))
pagoH=float(input("Ingrese el pago por hora: \n>"))

sBasico=horasT*pagoH
descuento=sBasico*0.12
sNeto=sBasico-descuento

print(f"Sueldo basico:  S/.{sBasico}")
print(f"Descuento :     S/.{descuento}")
print(f"Sueldo neto:    S/.{sNeto}")