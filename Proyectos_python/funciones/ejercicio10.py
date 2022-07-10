import time,os
os.system("cls")
time.sleep(1)

def Conversion_Tiempo():

    print("[1]:convertir horas a segundos.")
    print("[2]:convertir minutos a segundos.")
    print("[3]:convertir segundos a horas.")
    print("[4]:convertir segundos a minutos.")
    print("[0]:Para salir del programa.")
    print(" ")
    opc=int(input("Digite su opcion: "))
    if (opc==1):
        horas = int(input('Ingrese horas:'))
        conversion1 = (horas*3600)/1
        print(horas, "horas convertido a segundo son :", conversion1, " segundos")
    if(opc==2):
        minutos = int(input('Ingrese minutos:'))
        conversion2 = (minutos*60)/1
        print(minutos, " minutos convertidos a segundos son:", conversion2, "segundos")
    if(opc==3):
        segundos = int(input("Ingrese la cantidad de segundos:"))
        conversion1 = segundos/3600
        print(segundos, " segundos convertidos a horas son:", conversion1, " horas")
    if(opc==4):
        segundos = int(input("Ingrese la cantidad de segundos:"))
        conversion2 = segundos/60
        print(segundos, "segundos convertidos a minutos son:", conversion2, "minutos")
    if(opc==0):
        exit()

Conversion_Tiempo()

