# Escreva um programa que leia um número entre 0 e 9999, e mostre na tela cada um dos dígitos separados
def inputNumber():
    return input('Digite um número entre 0000 e 9999: ')


# SOLUÇÃO STRING
n = inputNumber()
if n.isdigit():
    print("Milhar: {}.".format(n[0]))
    print("Centena: {}.".format(n[1]))
    print("Dezena: {}.".format(n[2]))
    print("Unidade: {}.".format(n[3]))
else:
    print('Digite apenas números!')
    inputNumber()
