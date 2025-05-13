import os
os .system ("cls")

palavra = []

vogal = []

consol = []

y = 0

palavra = input("Digite uma palavra: \n")

tamanho = len(palavra)

for n in range(tamanho):
    ponteiro = palavra[y]

    palavra.append(ponteiro)

    if ponteiro == "a" or ponteiro == "A" or ponteiro == "E" or ponteiro == "e" or ponteiro == "I" or ponteiro == "i" or ponteiro == "O" or ponteiro == "o" or ponteiro == "U" or ponteiro == "u":
        vogal.append(ponteiro)
    else:
        consol.append(ponteiro)

    y = y + 1

vogalNum = len(vogal)

print(f"{vogalNum}")

carac = input("Digite um caractere (vogal ou consoante: \n)")

palavra["a"] = carac
palavra["A"] = carac
palavra["E"] = carac
palavra["e"] = carac
palavra["I"] = carac
palavra["e"] = carac
palavra["O"] = carac
palavra["o"] = carac
palavra["U"] = carac
palavra["u"] = carac

print(f"{palavra}")

