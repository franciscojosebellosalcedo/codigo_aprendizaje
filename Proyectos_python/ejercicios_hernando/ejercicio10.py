lista_numeros = [1, 30, 90, 800, 200]

opciones = 1
while opciones <= 4:
    temp = 0
    while temp < len(lista_numeros):
        if opciones == 1:
            if temp == 0:
                print("Numeros entre 0 y 10")
            if lista_numeros[temp] > 0 and lista_numeros[temp] < 10:

                print(lista_numeros[temp])
        if opciones == 2:
            if temp == 0:
                print("Numeros entre 11 y 100")
            if lista_numeros[temp] > 11 and lista_numeros[temp] < 100:

                print(lista_numeros[temp])
        if opciones == 3:
            if temp == 0:
                print("Numeros mayores que 80")
            if lista_numeros[temp] > 80:

                print(lista_numeros[temp])
        if opciones == 4:
            if temp == 0:
                print("Numeros menores que 30")
            if lista_numeros[temp] < 30:
                print(lista_numeros[temp])
        temp = temp + 1
    opciones = opciones + 1




