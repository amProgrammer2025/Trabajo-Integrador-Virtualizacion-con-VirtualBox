lista_notas = []

cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for nota in range(cant_alumnos):

    nota_ingresada = int(input(f"Ingrese la nota del alumno {nota+1}: "))
    lista_notas.append(nota_ingresada)

acum = 0

for nota in lista_notas:
    acum += nota

print(f"El promedio de notas entre los {cant_alumnos} es de: {acum / len(lista_notas)}")