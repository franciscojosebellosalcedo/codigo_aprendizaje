
def Suma_dinero():
	n=int(input('Digite la cantidad de numeros a sumar: '))
	acum=0
	for i in range(n):
		numero=int(input('ingrese:'))
		acum=acum+numero
	print(' ')
	print('  La suma total:  ', '$' ,acum)
Suma_dinero()