def notitas():
    print("Ingreso de notas...")
    
    nota1=float(input("Ingrese las nota 1: "))
    nota2=float(input("Ingrese las nota 2: "))
    nota3=float(input("Ingrese las nota 3: "))
    nota4=float(input("Ingrese las nota 4: "))

    if (nota1 < 0 or nota2 < 0 or nota3 < 0  or nota4 < 0) or (nota1 > 20  or nota2 > 20 or nota3 > 20  or nota4 > 20) :
        print("ERROR - Las notas son de 0 a 20: Reinicie programa")
    else:
        promedio=(nota4+nota1+nota2+nota3)/4
        if promedio>=0 and promedio<6:
            observacion="Bajo Rendimiento"
        elif promedio>=6 and promedio<10:
            observacion="Malo"
        elif promedio>=10 and promedio<15:
            observacion="Rendimiento Regular"
        elif promedio>=15 and promedio<18:
            observacion="Rendimiento Bueno"
        elif promedio>=18 and promedio<=20:
            observacion="Rendimiento Excelente"
        
        print(f"Observacion ---> {observacion}" )


def aplicacion():

    val=1

    codigo=(input("Ingrese su codigo: "))
    apellidos=(input("Ingrese sus apellidos: "))
    nombres=(input("Ingrese sus nombres: "))
    ciclo=(input("Ingrese el ciclo: "))

    
    if ciclo=="I":
        print("Curso 1 \t Curso 2 \t Curso 3 \t Curso 4")
        print("Windows \t Word \t\t Excel \t\t Access")
    elif ciclo=="II":
        print("Curso 1 \t Curso 2 \t Curso 3 \t Curso 4")
        print("Power Point \t Internet \t Extranet \t Intranet")
    elif ciclo=="III":
        print("Curso 1 \t\t  Curso 2 \t Curso 3 \t Curso 4")
        print("Visual Basic 6.0 \t.net 2019 -I \t SQL -I \t Analisis -I")
    elif ciclo=="IV":
        print("Curso 1 \t  Curso 2 \t Curso 3 \t Curso 4")
        print("Java I \t\t.net 2019 -II \t SQL -II \t Analisis -II")
    elif ciclo=="V":
        print("Curso 1 \t  Curso 2 \t Curso 3 \t Curso 4")
        print("Java II \tAsp .net 2019 \t Oracle -I \t Proyectos")
    elif ciclo=="VI":
        print("Curso 1 \t Curso 2 \t Curso 3 \t Curso 4")
        print("Java III \t Linux \t\t Php \t\t Sistemas")
    else: 
        val=0

    if val==0:
        print("Ciclo No Valido")
    else: 
        notitas()      
    
    

aplicacion()