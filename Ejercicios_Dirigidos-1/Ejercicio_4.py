precio_producto = int(input("Ingrese el precio del producto:   "))
cantidad_cuotas = int(input("Ingrese la cantidad de cuotas a pagar:   "))
interes = int(input("Ingrese el interes a cobrar:   "))

pago_cuotas=(precio_producto/cantidad_cuotas)+((interes/100)*precio_producto)
pago_neto= pago_cuotas*cantidad_cuotas
diferencia=pago_neto-precio_producto

print(f"El pago por cuota es: {pago_cuotas}")
print(f"Pago neto: {pago_neto} ")
print(f"Diferencia de pago si pagaba al contado: {diferencia}")