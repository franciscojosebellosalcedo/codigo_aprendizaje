import random
aux=0
dinero=10
while(  aux!=1):
	apuesta=int(input('¿Cuanto vas apostar?:'))
	while(apuesta==0 or apuesta <0 or apuesta>dinero):
		print('Error. \n Valor no correcto.')
		apuesta=int(input('¿Cuanto vas apostar?:'))
	adivina=input('¿Es par o impar?:')
	print('Elegiste :',adivina)
	dado1=random.randint(1,6)
	dado2=random.randint(1,6)
	suma=dado1+dado2
	print('\n')
	if(suma%2==0):
		print('Has ganado.')
		dinero=dinero+apuesta
		print('Ganaste :', '$',apuesta)
		print('Dinero: ',dinero)
	else:
		print('Has perdido.')
		dinero=dinero-apuesta
		print('Te quedan :' , '$'  ,dinero)
	if(dinero==0):
		print("Lo siento , te quedaste sin dinero.\nJUEGO TERMINADO.")
		break
	if(dinero>=500):
		print('Felicitaciones.\n Has alcanzado lo maximo en ganancia en el juego.')
		break
	print("\n")
	aux=int(input('¿Desea apostar mas ?.\n [0] 》Seguir.\n [1] 》Cerrar.\nDigite opcion:'))
	while(  aux<0 or aux >1):
		print('Error.\nIngrese una opcion valida.')
		aux=int(input('¿Desea apostar mas ?.\n [0] 》Seguir.\n [1] 》Cerrar.\nDigite opcion:'))
print('Programa finalizado.\n GRACIAS POR JUGAR.')
		
