print("***Bienvenido al sistema de calificacioness de su institución***")
nota1 = float(input("Ingrese la nota final de Matemáticas: "))
nota2 = float(input("Ingrese la nota final de Historia: "))
nota3 = float(input("Ingrese la nota final de Física: "))
nota4 = float(input("Ingrese la nota final de Biología: "))

promedio = (nota1 + nota2 + nota3 + nota4)/4

print("\nEl promedio de sus calificaciones es de: ", promedio, " sobre 10.\n¡Gracias!" )