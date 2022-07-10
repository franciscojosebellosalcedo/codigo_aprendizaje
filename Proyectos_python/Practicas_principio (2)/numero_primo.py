n=int(input('ingrese un numero :'))
if (n>1):
	cont=0
	for i in range(2,n):
		resto=n%i
		if (resto==0):
			cont=cont+1
	if(cont==0):
		print(n,'es primo.')
	else:
		print(n,'no es numero primo.')
		
else:
	print(n,'no es numero primo.')