
nota1=float(input("ingrese la primera nota de las practicas:"))
nota2=float(input("ingrese la segunda nota de las practicas:"))
nota3=float(input("ingrese la tercera nota de las practicas:"))
nota4=float(input("ingrese la cuarta nota de las practicas:"))

if(nota1<nota2 and nota1<nota3 and nota1<nota4):
    print("la primera nota fue eliminada",nota1)
    suma_notas=nota2+nota3+nota4
    promedio=suma_notas/3
    print("el promedio de las notas de las practica es de:",promedio)

if(nota2 < nota1 and nota2 < nota3 and nota2 < nota4):
    print("la segunda nota fue eliminada",nota2)
    suma_notas = nota1+nota3+nota4
    promedio = suma_notas/3
    print("el promedio de las notas de las practica es de:", promedio)

if(nota3<nota1 and nota3<nota2 and nota3<nota4):
    print("la tercera nota fue eliminada",nota3)
    suma_notas=nota2+nota1+nota4
    promedio=suma_notas/3
    print("el promedio de las notas de las practica es de:",promedio)

if(nota4 < nota1 and nota4 < nota2 and nota4 < nota3):
    print("la cuarta nota fue eliminada",nota4)
    suma_notas = nota2+nota3+nota1
    promedio = suma_notas/3
    print("el promedio de las notas de las practica es de:", promedio)
