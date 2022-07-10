import time
import os
os.system("cls")
time.sleep(1)
 
def Fiesta():
    aux=0
    catidad_personas =0
    integrantes=[ ]
    while(aux!=1):
        catidad_personas =catidad_personas+1
        print("---------FIESTA ISCO----------")
        nombre=input("Ingrese su nombre:")
        sexo=input("Ingrese sexo:")
        edad=int(input("Ingrese su edad:"))
        if(edad < 18):
            print("¡ No se aceptan menores de edad. !")
            print("SIGUIENTE PERSONA")
            Fiesta()
        integrantes.append([nombre,sexo,edad])
        aux=int(input("Digite 0 para permitir el ingreso \n Digite 1 para cerrar:"))

    cant_hombres=0
    cant_mujeres=0
    suma_edad_hombres=0
    suma_edad_mujeres=0
    for i in range(len(integrantes)):
        if(integrantes[i][1]=="masculino" ):
            cant_hombres=cant_hombres+1
            suma_edad_hombres=suma_edad_hombres+integrantes[i][2]
            promedio1=suma_edad_hombres/cant_hombres
        else:
            cant_mujeres=cant_mujeres+1
            suma_edad_mujeres = suma_edad_mujeres+integrantes[i][2]
            promedio2=suma_edad_mujeres/cant_mujeres
    print("Total de hombres:", cant_hombres)
    print("Total de mujeres:",cant_mujeres)
    print("El promedio total de las edades de las mujeres es:",promedio2)
    print("El promedio total de las edades de los hombres es:", promedio1)
    promedio_total = (suma_edad_hombres+suma_edad_mujeres)/catidad_personas
    print("Promedio total  de las edades es de:", promedio_total)
    print("Total de personas que ingresaron:",catidad_personas)
    
Fiesta()



    








