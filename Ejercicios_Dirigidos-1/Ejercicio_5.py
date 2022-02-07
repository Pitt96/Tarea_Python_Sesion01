def Ejercicio05(horas_normal,horas_extra,pago):

    sueldo_basico=horas_normal*pago

    extra=pago*1.15
    sueldo_extra=horas_extra*extra

    descuento=sueldo_basico*0.13

    sueldo_neto=sueldo_basico+sueldo_extra


    print(f"El sueldo basico: {sueldo_basico}")
    print(f"El sueldo extra: {sueldo_extra}")
    print(f"El descuento: {descuento}")
    print(f"El sueldo neto: {sueldo_neto}")



horas_normal=float(input("Ingrese las horas de trabajo normal: "))
horas_extra=float(input("Ingrese las horas de trabajo extra: "))
pago=float(input("Ingrese el pago por hora normal: "))
Ejercicio05(horas_normal,horas_extra,pago)