print("Asignatura algoritmos")

nota1=2.5
nota2=3.0
nota3=5.0
suma_notas=(nota1+nota2+nota3)
print("la suma total de las notas del estudiante es de:",suma_notas)
promedio1=(suma_notas)/3
print("el promedio de las notas del estudiante es de:",promedio1)

print("Asignatura informatica")

nota1=2.53
nota2=3.0
nota3=2.0
suma_notas=(nota1+nota2+nota3)
print("la suma total de las notas del estudiante es de:",suma_notas)
promedio2=(suma_notas)/3
print("el promedio de las notas del estudiante es de:",promedio2)

print("Asignatura base de datos")

nota1=3
nota2=2
nota3=3.7
suma_notas=(nota1+nota2+nota3)
print("la suma total de las notas del estudiante es de:",suma_notas)
promedio3=(suma_notas)/3
print("el promedio de las notas del estudiante es de:",promedio3)


suma_de_promedios=(promedio1+promedio2+promedio3)
print("la suma de los promedios de las asignaturas es de:",suma_de_promedios)
promedio_total=suma_de_promedios/3
print("promedio total de las asignaturas del estudiante es de:",promedio_total)
if(promedio_total>=3):
    print("el estudiante gano el semestre")
else :
    print("el estudiante perdio el semestre")
