import time
import os
os.system("cls")
time.sleep(1)

# def Automotores():
#     automotores=["vehiculos","camiones","tractomulas"]
#     valores=[350,1200,1600]
#     cont=[0,0,0]
#     acum=[0,0,0]

#     ingrese=int(input("Ingrese un automotor:"))
#     while(ingrese!=0):
#         if (ingrese>len(automotores)):
#             print("error de ingreso.")
#             ingrese = int(input("Ingrese un automotor:"))
#         precio=valores[ingrese-1]
#         cont[ingrese-1] = cont[ingrese-1]+1
#         acum[ingrese-1] = acum[ingrese-1]+precio
#         ingrese = int(input("Ingrese un automotor:"))
#     total_dia=0
#     for i in range(len(acum)):
#         total_dia = total_dia+acum[i]
#     for x in range(len(automotores)):
#         auto=automotores[x]
#         acumulado_auto=acum[x]
#         print(auto,":","acumulado","$",acumulado_auto)
#     print("El total recaudado en el dia fue de:", "$", total_dia)
#     maximo=0
#     for c in range(len(cont)):
#         if(cont[c]>maximo):
#             maximo=cont[c]
#     posmaximo=cont.index(maximo)
#     autopos=automotores[posmaximo]
#     print("El automotor que mas transcito fue:",autopos)


# Automotores()



# def TotalSalario():
#     trabajadores=[ ]
#     aux=0
#     cantidad=0
#     while(aux!=1):
#         cantidad = cantidad+1
#         print("Trabajador:",cantidad)
#         nombre=input("Ingrese el nombre del trabajador:")
#         h_tra=int(input("ingrese las horas trabajadas:"))
#         salario=int(input("ingrese el salario que recibira este trabajador:"))
#         print("\n")
#         trabajadores.append([nombre,h_tra,salario])
#         aux=int(input("ingrese 0 para agregar mas trabajadores \n ingrese 1 para cerrar el programa:"))
        
#     total_salario=0
#     for i in range(len(trabajadores)):
#         total_salario=total_salario+trabajadores[i][2]
#         print("Trabajador", (i+1), "Nombre:", trabajadores[i][0], "Salario:","$", trabajadores[i][1]*trabajadores[i][2])
#     print("La suma de los salarios es de :","$",total_salario)

# TotalSalario()



