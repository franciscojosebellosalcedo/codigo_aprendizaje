import time
import os
os.system("cls")
time.sleep(1)

estudiantes=[ ]
cant_estudiantes=10
aux=0
while(aux<cant_estudiantes):
    nombre=input("ingrese su nombre:")
    nota=float(input("ingrese su nota correspondiente:"))
    if (nota>10 ):
        print("¡ ERROR ! Las notas van del 1 hasta el 10, (no se aceptan numeros decimales).")
        nota = float(input("ingrese su nota correspondiente:"))
    estudiantes.append([nombre,nota])
    aux=aux+1
cont1=0
cont2=0
cont3=0
cont4=0
for i in range(len(estudiantes)):

    if (estudiantes[i][1]<5.0):
        cont1=cont1+1
    if(estudiantes[i][1] >= 5.0 and estudiantes[i][1]<7.0):
        cont2=cont2+1
    if(estudiantes[i][1] >= 7.0 and estudiantes[i][1]<8.0):
        cont3=cont3+1
    if(estudiantes[i][1]>=8.0):
        cont4=cont4+1
print("Notas menores que 5.0:",cont1)
print("Notas de 5.0 o mas pero menor que 7.0 :",cont2)
print("Notas 7.0  o mas pero menor que 8.0 :",cont3)
print("Notas de 8.0 o mas de 8.0 :", cont4)







