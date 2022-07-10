arreglo=[ ]
mayor=0
vuelta=0


while(vuelta<=4):
	vuelta=vuelta+1
	numero=int(input('ingrese un valor :'))
	arreglo.append(numero)
	tamaño=len(arreglo)
for i in range(0,len(arreglo)):
	if(arreglo[i]>mayor):
		mayor=arreglo[i]


print('el tamaño del arreglo es  ',tamaño) 
print('el numero mayor es :',mayor)

resto=mayor%2
if(resto==0):
	print('el numero mayor es par')
else:
	print('el numero mayor es impar')







	

