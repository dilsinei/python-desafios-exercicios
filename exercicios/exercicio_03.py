import os
import time


def limpar_tela():
    time.sleep(5)
    os.system("cls")


####################################################################################################
####################################################################################################
# calcular a media de uma lista de numeros
numeros = [10, 5, 10, 15, 5]


def calcular_media_iniciante(numeros):
    soma = 0
    media = 0
    for numero in numeros:
        soma = soma + numero

    media = soma / len(numeros)
    print(
        f"A lista contém {len(numeros)} items, a soma dos numeros é: {soma} e a média é igual a: {media}"
    )


####################################################################################################
print("=" * 100)
calcular_media_iniciante(numeros)

####################################################################################################


def calcular_media(numeros):
    if not numeros:
        return "A lista está vazia."
    return sum(numeros) / len(numeros)


####################################################################################################
print("=" * 100)
print(f"A média é igual a: {calcular_media(numeros)}")


####################################################################################################
# Verificar se um número é par ou ímpar: Desenvolva um programa que receba um número como entrada e
#   determine se ele é par ou ímpar.
def par_ou_impar():
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é impar.")


####################################################################################################
print("=" * 100)
par_ou_impar()


####################################################################################################
# Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit.
def converter_celsius_fahrenheit():
    temperatura = int(input("Digite a temperatura em celsius: "))
    temp_fahrenheit = (temperatura * 1.8) + 32
    print(f"{temperatura}°C é igual a {temp_fahrenheit}°F")


####################################################################################################
print("=" * 100)
converter_celsius_fahrenheit()

####################################################################################################
# Crie uma função que calcule o fatorial de um número dado como entrada.


def fatorial():
    numero = int(input("Digite um numero:"))

    if numero < 0:
        return "Fatorial não definido para números negativos."
    elif numero == 0:
        return 1
    else:
        contador = 1
        fatorial = 1
        while contador <= numero:
            fatorial = fatorial * contador
            contador += 1
        return fatorial


resultado = fatorial()

####################################################################################################
print(resultado)
print("=" * 100)

####################################################################################################
# Implemente um programa que verifique se uma palavra é um palíndromo, ou seja,
# se pode ser lida da forma tanto da esquerda para a direita quanto da direita para a esquerda.
####################################################################################################

# print("=" * 100)
####################################################################################################
# Desenvolva uma função que receba uma palavra como entrada e retorne a quantidade de vogais.
####################################################################################################

# print("=" * 100)
####################################################################################################
# Escreva um programa que encontre o maior elemento em uma lista de números.
####################################################################################################

# print("=" * 100)
####################################################################################################
# Crie uma função que receba uma lista de números como entrada e ordene em ordem crescente.
####################################################################################################

# print("=" * 100)
####################################################################################################
# Implemente um programa que verifique se um número é primo, divisível apenas por 1 e por ele mesmo.
####################################################################################################

# print("=" * 100)
####################################################################################################
# Desenvolva uma função que calcule o valor final de um investimento com base em uma taxa de juros
# e um período de tempo.

####################################################################################################

# print("=" * 100)
####################################################################################################


limpar_tela()
