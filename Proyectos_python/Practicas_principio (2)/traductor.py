
español=['hola','tu','perro','gato','verde','azul','casa','raton','feliz','enojado','patetico','programador','amor','principe ','papá','mamá','hermosa','amiga','amigo','hermano','hermana','novia','novio']

coreano=[ '안녕하세요 : annyeonghaseyo ',' 당신 :dangsin','   개 : gae  ',' 고양이 : goyang-i ','  초록 : cholog  ',' 푸른 : puleun   ', '  집: jib ',' 쥐 : jwi ','  행복: haengbog  ','  괴로운 : goeloun   ','   서투른 : seotuleun ','  프로그램 제작자 : peulogeulaem jejagja ','   사랑 : salang ', ' 왕자 : wangja  ','  아버지 : abeoji  ','  엄마 : eomma ','  아름다운 : aleumdaun ','  친구 : chingu ','  친구 : chingu ', ' 동료 : donglyo  ','여자 형제 : yeoja hyeongje   ','  여자 친구 : yeoja chingu ','  신랑 : sinlang  ']

aux=0
cont=0
while(aux!=1):
	for x in range(len(español)):
		print(x+1,español[x])
	print("\n")
	palabra=input('Ingrese la palabra que quiere traducir :')
	for i in range(len(español)):
		if(palabra==español[i]):
			print(' La palabra ',palabra,'Traducido a coreano es :',coreano[i])
	cont=cont+1
	print('\n')
	aux=int(input('Ingrese 0 para seguir traduciendo \n ingrese 1 para cerrar.'))
print(cont,'palabras traducidas.')