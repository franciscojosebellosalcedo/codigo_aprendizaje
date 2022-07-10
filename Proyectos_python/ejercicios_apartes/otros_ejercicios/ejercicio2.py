import os,time
os.system("cls")
time.sleep(1)
numeros=[ ]
for i in range(1,6):
    n=int(input(" ingrese un valor:"))
    numeros.append(n)
suma=0
for f in range(len(numeros)):
    suma=(suma+numeros[f])
    promedio=(suma/len(numeros))
print("El promedio de los cinco numeros ingresados es de:",promedio)

