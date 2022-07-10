import os
import time
import random
os.system(" cls")
time.sleep(1)



total=10
cont1=0
apuesta=1
while(apuesta!=0):
    apuesta=int(input("¿Cuanto desea apostar?: "))
    if(apuesta==0):
        exit()
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    suma_dados=dado1+dado2
    resto_suma=suma_dados%2

    adivina=input("¿Es par o impar?: ")

    if (adivina=="par"):
        if(resto_suma==0):
            cont1=cont1+1
            resul = total+apuesta
            print("Ganaste:","$",resul)
        else:
            print("Has perdido.")
            resul = total-apuesta
            print("Te quedan:","$",resul)

    if (adivina == "impar"):
        if(resto_suma != 0):
            cont1 = cont1+1
            resul = total+apuesta
            print(" Ganaste :","$", resul)
        else:
            print("Has perdido.")
            resul = total-apuesta
            print("Te quedan:", "$", resul)

        if(resul<0):
            exit()
            print("Se te acabo tu dinero.")

print("Partidas ganadas:",cont1)
        

