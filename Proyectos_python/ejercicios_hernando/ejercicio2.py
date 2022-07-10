# numero1=int(input("ingrese un valor:"))
# numero2=int(input("ingrese un valor:"))

# if(numero1>numero2 and numero2<numero1):
#     print("el pimer numero es el mayor")

# if(numero2>numero1 and numero1<numero2):
#     print("el segundo numero es el mayor")



# segunda forma

arreglo=[]
mayor=0
numero1=int(input("ingrese un valor:"))
numero2=int(input("ingrese un valor:"))
arreglo.append(numero1)
arreglo.append(numero2)

for i in range(len(arreglo)):
    if(arreglo[i]>mayor):
        mayor=arreglo[i]
print("el numero mayor es:",mayor)