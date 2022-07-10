

aux=0
salon=[ ]
cont=0
while(aux!=1):
	cont=cont+1
	nombre=input('Ingrese el nombre del estudiante : ')
	nota1=int(input('Digite la primera nota: '))
	nota2=int(input('Digite la segunda nota: '))
	nota3=int(input('Digite la tercera nota: '))
	salon.append([nombre,nota1,nota2,nota3])
	print('  ')
	aux=int(input('Ingrese 0 para agregar estudiante \n Ingrese 1 para cerrar el programa :  '))
print('Total de estudiantes ingresados : ',cont)

for i in range( len(salon) ):
	print('Estudiante : ' ,salon[i][0],'Promedio de notas : ' ,(salon[i][1]+salon[i][2]+salon[i][3])/3)

	
	