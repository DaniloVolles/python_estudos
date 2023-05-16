# Escreva um programa que me informe o dobro, o triplo, e a raiz quadrada de um número.

import math

n = int(input("Informe um Número Inteiro: "))

dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n) #seria possível resolver isso também assim: r = n**(1/2)

print("O dobro de {} é {}.".format(n, dobro))
print("O triplo de {} é {}.".format(n, triplo))
print("A raíz quadrada de {} é {:.2f}.".format(n, raiz))
