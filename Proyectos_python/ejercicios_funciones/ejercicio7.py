# EJERCICIO 1
# 
# n=0
# lista_numeros=[]

# while( n<10):
#     n=n+1
#     numeros=int(input("ingrese un numero:"))
#     lista_numeros.append(n)
# for i in range(len(lista_numeros)):
#     numero=lista_numeros[i]
#     print("indice",i,"_","valor correspondiente",":",numero)

# EJERCICIO 2

# lista_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# print("_____________________________________________________________________________________________________________________________________")
# print(lista_n)
# print("_____________________________________________________________________________________________________________________________________")

# n=len(lista_n)
# suma=sum(lista_n)
# print("la suma de todos los numeros dentro de la lista es de:",suma)
# media=suma/n
# print("la media es de:",media)

    

# EJERCICIO 3

ac = [ ]
c1 = True
print("_____________________________________________________________________________________________________________________________________")
Letra = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
         "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "y", "Z"]
print(Letra)
while(True == c1):
    id = int(input("Ingrese la posicion: "))
    while(id >= 27 or id <= -2):
        print("Introducir un dato valido: ")
        id = int(input("Ingrese la posicion  : "))
    ac.append(id)
    if(id == -1):
        ac.pop()
        for i in range(0, len(ac)):
            print("Posicion", ac[i], "se encuentra la letra", Letra[ac[i]])
            if(i+1 == len(ac)):
                c1 = False


