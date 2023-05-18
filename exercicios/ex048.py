# Faca um programa que calcule a soma de todos os números impares que são múltiplos de 3 entre 1 e 500.

s = 0
for a in range(1, 100):
    if a % 2 == 0:
        continue
    elif a % 3 != 0:
        continue

    s += a
    print(s)
print(s)
