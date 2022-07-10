import time
import os
time.sleep(1)
os.system("cls")

def Media_temperatura(cantidad_dias):
    aux=0
    while(aux < cantidad_dias):
        aux=aux+1
        temperatura_maxima=int(input("Ingrese la temperatura maxima del dia:" ))
        temperatura_manima = int(input("Ingrese la temperatura minima del dia: "))
        promedio_temperatura=(temperatura_maxima+temperatura_manima)/2
        print(" ")
        print("La media de la temperatura del dia",aux,"es:", promedio_temperatura)
        print(" ")

Media_temperatura(5)
