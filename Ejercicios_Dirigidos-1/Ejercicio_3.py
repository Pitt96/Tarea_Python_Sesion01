#from turtle import st
def notas():
    curso=input("Ingrese el nombre del curso, por favor: ")
    nota1 = int(input("Ingrese su primera nota, por favor "))
    nota2 = int(input("Ingrese su segunda nota, por favor "))
    nota3 = int(input("Ingrese su tercera nota, por favor "))
    nota4 = int(input("Ingrese su cuarta nota, por favor "))
    nota5 = int(input("Ingrese su quinta nota, por favor "))
    nota6 = int(input("Ingrese su sexta nota, por favor "))
    promedio=(nota1+nota2+nota3+nota5+nota6)/6
    print("Curso: "+str(curso))
    print("Nota 1: "+str(nota1))
    print("Nota 2: "+str(nota2))
    print("Nota 3: "+str(nota3))
    print("Nota 4: "+str(nota4))
    print("Nota 5: "+str(nota5))
    print("Nota 6: "+str(nota6))
    print("Promedio: "+str(promedio))
notas()