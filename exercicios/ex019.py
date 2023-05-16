# Crie um programa que sorteie um ítem em uma lista
import random

n1 = input("n1 = ")
n2 = input("n2 = ")
n3 = input("n3 = ")
n4 = input("n4 = ")

lista = [n1, n2, n3, n4]

print("A lista de ítens é ['{}', '{}', '{}', '{}'].".format(n1, n2, n3, n4))

sorteio = random.choice(lista)

print("Item sorteado: ", sorteio)
