import random
randomNumber = random.randint(0, 10)
randomPlus = random.randint(1, 5)
randomLess = random.randint(1, 5)
print(f"Esse numero é menor que {randomNumber + randomPlus} e é maior que {randomNumber - randomLess}")
inputOfUser = int(input("Eu gerei um numero aleatório, advinhe qual é \n "))
if inputOfUser == randomNumber:
    print(f"Você acertou")
else:
    print(f"Você errou o numero é {randomNumber}")