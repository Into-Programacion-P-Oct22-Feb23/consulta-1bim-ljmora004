plan = int(input("Seleccione su plan de Spotify: \n1.Individual\n2.Duo\n3.Familiar\n" ))
adicion = 0
costo = 15
valorPagar = 0

if plan == 1:
	valorPagar = costo
	print("\nEl valor a pagar por el plan que escogió es: $", valorPagar)
elif plan == 2:
	adicion = (costo * 5)/100
	valorPagar = costo + adicion
	print("\nEl valor a pagar por el plan que escogió es: $", valorPagar)
elif plan == 3:
	adicion = (costo * 10)/100
	valorPagar = costo + adicion
	print("\nEl valor a pagar por el plan que escogió es: $", valorPagar)
else:
	print("\nLa opción que escogió no existe, por favor intentelo de nuevo.\nGracias")
