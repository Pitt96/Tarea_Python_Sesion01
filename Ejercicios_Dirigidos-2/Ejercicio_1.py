def Descuento(sueldo,porcentaje):
    return sueldo*porcentaje
def Bonificacion(sueldo,porcentaje):
    return sueldo*porcentaje
def Mostrar(sueldo,descuento1,descuento2,bonificacion1,bonificacion2):
    print("********************************************\nNombre : "+nombre)
    print("Ocupacion: "+ocupacion)
    print(f"Sueldo: {sueldo}")
    print(f"Descuento 1: {descuento1}")
    print(f"Descuento 2: {descuento2}")
    print(f"Bonificacion 1: {bonificacion1}")
    print(f"Bonificacion 2: {bonificacion2}")

ocupacion=""
sueldo=0
val=0

nombre=input("Ingrese el nombre del trabajador:\n>")
categoria=int(input("Escoge la categoria que pertenece:"+
"\n1 --> A\n2 --> B\n3 --> C\n4 --> D\n5 --> E\n6 --> Otros\n>"))

if categoria == 1:
    ocupacion="Analista"
    sueldo=2500
    por1=0.12
    por2=0.10
    boni1=0.14
    boni2=0.16
elif categoria == 2:
    ocupacion="Programador"
    sueldo=1500
    por1=0.1
    por2=0.08
    boni1=0.12
    boni2=0.14
elif categoria == 3:
    ocupacion="Asistente"
    sueldo=1000
    por1=0.08
    por2=0.06
    boni1=0.10
    boni2=0.12
elif categoria == 4:
    ocupacion="Tecnico"
    sueldo=700
    por1=0.06
    por2=0.04
    boni1=0.08
    boni2=0.10
elif categoria == 5:
    ocupacion="Operador"
    sueldo=500
    por1=0.04
    por2=0.02
    boni1=0.06
    boni2=0.08
else:
    val=1

if val==1 :
    print("Categoria no valida.")
else:
    descuento1=Descuento(sueldo,por1)
    descuento2=Descuento(sueldo,por2)
    bonificacion1=Bonificacion(sueldo,boni1)
    bonificacion2=Bonificacion(sueldo,boni2)
    Mostrar(sueldo,descuento1,descuento2,bonificacion1,bonificacion2)
