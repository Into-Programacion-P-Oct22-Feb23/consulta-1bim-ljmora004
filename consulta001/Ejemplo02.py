nombre = input("Cuál es el nombre de su mascota: ")
raza = input("Cuál es la raza de su mascota: ")
peso = float(input("Cuál es el peso de su mascota: "))
consulta = 8

valorPagar = peso * consulta

print("\nSu mascota " + nombre + " \nDe raza: " + raza + "\nCon un peso de: ", peso, 
	" libras" + "\nTiene una consulta por el valor de: ", valorPagar, "dólares")