def multiplo(n1,n2):
	resto=n1%n2
	if resto==0:
		print(" El numero ",n1,'es multiplo del numero',n2)
		print(' ')
		print('Resto:')
		return resto
		
	if resto !=0:
		print(" El numero",n1,'no es multiplo del numero',n2)
		print(' ')
		print('Resto:')
		return resto
solucion=multiplo(3,2)
print(solucion)