nombre = input("Nombre del estudiante:")
edad= int(input("Edad del estudiante:"))
nota1 = float(input("Ingrese la primera nota:"))
nota2 = float(input("Ingrese la segunda nota:"))
nota3 = float(input("Ingrese la tecera nota:"))
promedio = (nota1 + nota2 + nota3)/3
if promedio >= 71 : 
    print("Aprobado")
else: 
 print("No aprobado")