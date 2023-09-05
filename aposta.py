#Crie um jogo em Python onde o programa escolhe um número aleatório e o jogador precisa adivinhar qual é o número correto.

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 50)
    tentativas = 0

    while True:
        aposta = int(input("Digite um número: "))
        tentativas += 1

        if aposta == numero_secreto:
            print("Parabéns! Você acertou o número em", tentativas, "tentativas.")
            break
        elif aposta < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

jogo_adivinhacao()