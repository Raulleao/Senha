import numbers
import random
import string


def password_generator(len_pass=8):
    ascii_options = string.ascii_letters
    numbers_options = string.digits
    punt_options = string.punctuation

    somaTudo = ascii_options+numbers_options+punt_options

    password_user = ""

    for cont in range(0, len_pass):
        digit = random.choice(somaTudo)
        password_user += digit
    return password_user


choice_user = input("Quantos digitos na senha: ")
if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada Inválida")
    quit()
response = password_generator(choice_user)
print(f"Senha gerada:\n{response}")
