
print('PRIMERA MATRIZ')
m1=[[1,2,3],[4,5,6]]
m2=[[1,2,3],[4,5,6]]
for i in range(len(m1)):
	for f in range(len(m1[i])):
		print(m1[i][f],end=" ")
	print(' ')
	
print('SEGUNDA MATRIZ')

m1=[[1,2,3],[4,5,6]]
m2=[[1,2,3],[4,5,6]]
for i in range(len(m2)):
	for f in range(len(m2[i])):
		print(m2[i][f],end=" ")
	print(' ')
	
print('SUMA MATRIZ')
for i in range(len(m1)):
	for f in range(len(m2[i])):
		suma=m1[i][f]+m2[i][f]
		print(suma,end=' ')
	print(' ')
	

