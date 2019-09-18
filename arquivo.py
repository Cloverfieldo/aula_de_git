import random
randomNumber = random.randint(0, 10)
inputOfUser = input("Eu gerei um numero aleatório, advinhe qual é ")
if inputOfUser == randomNumber:
    print(f"Você acertou")
else:
    print(f"Você errou o numero é {randomNumber}")