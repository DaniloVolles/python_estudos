# Escreva um programa que determine a tabuada de um número

n = int(input("informe um número inteiro: "))

i = 1
while i < 11:
    r = n * i
    print("{} x {} = {}".format(n, i, r))
    i += 1

print("Obrigado!")
