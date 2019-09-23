word = str(input("Uma palavra para eu contar "))
counting = int(input("Quantas letras você quer saber"))
if len(word) == counting:
    print(f"Sim essa palavra tem {counting}")
else:
    print(f'Essa palavra tem {len(word)} não {counting}')
