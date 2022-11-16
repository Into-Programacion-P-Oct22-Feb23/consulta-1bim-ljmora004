print("¡Bienvenido al sistema de cobro de planilla de luz!")
edad = int(input("Ingrese su edad: "))
consumo = float(input("Ingrese el consumo mensual de luz en K/H: "))
costo_mes = float(input("Ingrese el costo por K/H: "))
descuento = 20
valorPagar = 0
subTotal = consumo * costo_mes

if edad >= 65:
	descuento = (subTotal * descuento)/100
	valorPagar = subTotal - descuento
	print("El subtotal a pagar es de: ", subTotal)
	print("El valor final a pagar es de: ", valorPagar)
else:
	valorPagar = subTotal
	print("El subtotal a pagar es de: $", subTotal)
	print("El valor final a pagar es de: $", valorPagar)


