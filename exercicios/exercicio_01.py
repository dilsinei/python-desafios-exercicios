palavra = input("Digite uma palavra: ")


def reverte_palavra(palavra):
    palavra_invertida = ""
    # Para cada 'ITEM" na LISTA
    for letra in palavra:
        palavra_invertida = letra + palavra_invertida
    print(palavra_invertida)
    return 0


reverte_palavra(palavra)
print("=" * 50)
# hack python manipulação de string
palavra_invertida = palavra[::-1]

print(palavra_invertida)
