#m1=[[1,2,3],[3,2,1]]
#m2=[[5,6,5],[6,7,8]]
#print('MATRIZ 1')

#for i in range(len(m1)):
#	for f in range(len(m1[i])):
#		print(m1[i][f],end=' ')
#	print( ' ')		
#print(' MATRIZ 2')
#	
#for i in range(len(m2)):
#	for f in range(len(m2[i])):
#		print(m2[i][f],end=' ')
#	print(' ')
#	
#print('SUMA DE LAS MATRICES')

#for i in range(len(m1)):
#	for f in range(len(m2[i])):
#		suma=m1[i][f]+m2[i][f]
#		print(suma,end=' ')
#	print(' ')

m1=[[1,8,10],[3,6,9]]
suma=0
for i in range(len(m1[0])):
	suma=suma+m1[0][i]
print(suma)
print('_____')
for o in range(len(m1[1])):
	suma=suma+m1[1][o]
print(suma)
	
	




	