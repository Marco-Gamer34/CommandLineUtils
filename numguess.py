import random
print("Chute o número!")
print("Dificuldades:\n1 - Fácil\n2 - Médio\n3 - Difícil\n4 - IMPOSSÍVEL\n5 - INFINITO!!!")
dificu = int(input(": "))
if dificu == 1:
	limit = 50
if dificu == 2:
	limit = 100
if dificu == 3:
	limit = 500
if dificu == 4:
	limit = 5000
if dificu == 5:
	limit = 9999999999999
numero = random.randint(0, limit)
while True:
	guess = int(input("Chute: "))
	if guess < numero:
		print("Mais!") 
	if guess > numero:
		print("Menos!")
	if guess == numero:
		print("Isso aí! =)")
		input()
		exit()