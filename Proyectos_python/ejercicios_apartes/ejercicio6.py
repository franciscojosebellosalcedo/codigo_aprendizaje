aux=0
numeros=[ ]
while( aux<3):
    n=int(input(" ingrese:"))
    numeros.append(n)
    aux=aux+1
print(numeros)
menor=numeros[0]
for i in range(len(numeros)):
    if( numeros[i]<menor):
        menor=numeros[i]
print("El numero menor de la lista es:",menor)     

mayor = numeros[0]
for i in range(len(numeros)):
    if(numeros[i] >mayor):
        mayor = numeros[i]
print("El numero mayor de la lista es:", mayor)






    
  





