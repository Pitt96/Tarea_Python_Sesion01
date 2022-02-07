def sueldoEmpleado(sueldo):
    aumento=200
    bonificacion=sueldo*0.10
    total=sueldo+aumento+bonificacion
    print("El aumento del sueldo es :"+str(aumento))
    print("La bonificaacion es : "+str(bonificacion))
    print("El sueldo total es: "+str(total))

cash=int(input("Ingrese su sueldo por favor: \n>"))
sueldoEmpleado(cash)