#numeros=[ ]
#acumulador=0
#while( acumulador<3):
#	acumulador=acumulador+1
#	n=int(input('ingrese un valor:'))
#	numeros.append(n)
#print(numeros)



#indice=0
#while(indice<len(numeros) ):
#	print('indice:', indice,'__','valor:',numeros[indice])
#	indice=indice+1

#for i in range(len(numeros) ):
#	print('indice:', i,'__','valor:',numeros[i])


frutas=[' mamones',' limones','papayas' ]
print(frutas)

cant_frutas=[ ]
acumulador=0
while( acumulador<1):
	acumulador=acumulador+1
	fruta1=int(input('ingrese la cantidad de mamomes que tienes:'))
	cant_frutas.append(fruta1)
	fruta2=int(input('ingrese la cantidad de limones  que tienes:'))
	cant_frutas.append(fruta2)
	fruta3=int(input('ingrese la cantidad de papayas que tienes:'))
	cant_frutas.append(fruta3)

print('listado segun su valores ingresados anteriormente:')
for i in range ( len(frutas)):
	print(' fruta: ',' 》》' ,frutas[i],' 》', 'Cantidad de frutas:',' 》》',cant_frutas[i])



	
	
