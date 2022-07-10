matriz=[]
import os,time
time.sleep(1)
os.system("cls")
aux=0
pregunta=int(input("¿Cuantas  personas va a registrar?:"))
while(aux<pregunta):
    aux=aux+1
    print("Persona numero:",aux)
    sexo=input("Ingrese su sexo:")
    nombre=input("Ingrese su nombre:")
    apellido=input("Ingrese su apellido:")
    edad=int(input("Ingrese su edad:"))
    while(edad <= 0 or edad >= 130):
        print("Error. Edad incorrecta.")
        edad = int(input("Ingrese la edad nuevamente:"))
    dni=int(input("Ingrese su DNI:"))
    while(dni<=0):
        print("DNI invalido.")
        dni=int(input("Ingrese su DNI nuevamente:"))
    matriz.append([sexo,nombre,apellido,edad,dni])
    print("\n")

for i in range(0,len(matriz)):
    print( "Sexo:",matriz[i][0],"\n",
            "Nombre:",matriz[i][1],"\n",
            "Apellido:",matriz[i][2],"\n",
            "Edad:",matriz[i][3],"\n",
            "DNI:",matriz[i][4])
    if(matriz[i][3]>=18):
        print(matriz[i][1],"eres mayor de edad.")
        print("\n")
    else:
        print(matriz[i][1],"eres menor de edad.")
        print("\n")

print("\n")
cantHombres=0
for i in range(len(matriz)):
    if(matriz[i][0]=="m" or matriz[i][0]=="M" or matriz[i][0]=="masculino"):
        cantHombres=cantHombres+1
print("Total de hombres:",cantHombres)
cantMujeres = 0
for i in range(len(matriz)):
    if(matriz[i][0] == "f" or matriz[i][0] == "F" or matriz[i][0] == "femenino"):
        cantMujeres = cantMujeres+1
print("Total de mujeres:", cantMujeres)
print("Total de personas registradas:",aux)


  
