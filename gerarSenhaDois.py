from itertools import combinations_with_replacement
import string
import time
import sys
from datetime import timedelta
from random import seed, random


def main(args):
    valores = string.ascii_letters
    valores += string.digits
    valores += string.punctuation
    tamanho = 5

    init = time.time()
    gerar_senhas(valores, tamanho)
    final = time.time()

    print(str(f"{final-init:.2f}")+"s")


def gerar_senhas(valores, tamanho):
    comb = combinations_with_replacement(valores, tamanho)
    print(len(list(comb)))


if __name__ == "__main__":
    main(sys.argv[1:])
