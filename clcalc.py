result = 0
while True:
	print("#"*32)
	print("# Resultado                    # = {0}".format(result))
	print("#"*32)
	operador = input("+, -, *, /, //, **, %")
	n1 = int(input("1: "))
	n2 = int(input("2: "))
	if operador == "+":
		result = n1 + n2
	if operador == "-":
		result = n1 - n2
	if operador == "*":
		result = n1 * n2
	if operador == "/":
		result = n1 / n2
	if operador == "//":
		result = n1 // n2
	if operador == "**":
		result = n1 ** n2
	if operador == "%":
		result = n1 % n2
	print("\n"*37)