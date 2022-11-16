nombre = input("Ingrese su nombre: ")
salario = int(input("Ingrese su salario: "))
años = int(input("Ingrese cuántos años lleva en la empresa: "))
bono = 0
sueldo_final = 0

if años >= 3 and años < 10:
	bono = (salario * 10)/100
	sueldo_final = salario + bono
	print("\n" + nombre + " con ", años, " años trabajando en la empresa.\nTiene derecho a un bono de: $", bono)
	print(nombre + " su salario final es de: $", sueldo_final)
elif años >=10 and años < 25:
	bono = (salario * 20)/100
	sueldo_final = salario + bono
	print("\n" + nombre + " con ", años, " años trabajando en la empresa.\nTiene derecho a un bono de: $", bono)
	print(nombre + " su salario final es de: $", sueldo_final)
elif años >= 25:
	bono = (salario * 30)/100
	sueldo_final = salario + bono
	print("\n" + nombre + " con ", años, " años trabajando en la empresa.\nTiene derecho a un bono de: $", bono)
	print(nombre + " su salario final es de: $", sueldo_final)
else:
	print("\nLo sentimos, no ha trabajado los años suficientes en la empresa para tener derecho a un bono.")