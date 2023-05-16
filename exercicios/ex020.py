# Crie um programa que sorteie a ordem de apresentação de uma lista
import random

a = input("Primeiro item: ")
b = input("Segundo item: ")
c = input("Terceiro item: ")
d = input("Quarto item: ")

lista = [a, b, c, d]

random.shuffle(lista)

print(lista)
