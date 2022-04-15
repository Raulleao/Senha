from random import random, choice
import string
import time
# usuário pode digitar a sua própria senhaUsuario ou escolher a que o programa sugerir

tamanho = 10
valores = string.ascii_letters  # todas as letras mas e min
valores += string.digits  # numeros de 0 a 9
valores += string.punctuation  # caracteres especiais


def apresentacao(boasVindas):  # Programa irá apresentar a mensagem de Boas Vindas
    print("\033[34m="*30)
    print(boasVindas)
    print("\033[34m=\033[m"*30)


def gerarSenhas(valores):
    global senhaGerada
    senhaGerada = ""
    for cont in range(tamanho):
        senhaGerada += choice(valores)
    len(senhaGerada)


def quebrarSenha(valores):
    global senhaEncontrada
    senhaEncontrada = ""
    while(len(senhaEncontrada) != tamanho):
        caracteresEncontrados = len(senhaEncontrada)
        caracter = choice(valores)
        if (caracter == senhaGerada[caracteresEncontrados]):
            senhaEncontrada += caracter
            print(senhaEncontrada)
            time.sleep(0.5)
    print(f"\033[31mSENHA GERADA:\n{senhaGerada}")
    print(f"\033[34mSENHA HACKEADA:\n{senhaEncontrada}")


apresentacao("===== Seja Bem-vindo(a) ======")

gerarSenhas(valores)
print()
quebrarSenha(valores)
print()
