for c in range(1, 6):
    print(c, '- Danilo') #Nesse caso vai ser impresso 5x: "6 - 1 = 5"
print('-- FIM --')

for c in range(0, 5):
    print(c)
print('-- FIM --')

for c in range(5, 0, -1):
    print(c)
print('-- FIM --')

for c in range(0, 10, 2):
    print(c)
print('-- FIM --')

# Trabalhando com Input
# n = int(input('Digite um número inteiro: '))
# for c in range(0, n, 5):
#     print(c)
# print('-- FIM --')
#
# a = int(input('Digite o início: '))
# b = int(input('Digite o passo: '))
# c = int(input('Digite o final: '))
# for c in range(a, b+1, c):
#     print(c)
# print('-- FIM --')

s = 0
for c in range(0, 4):
    n = int(input(f"Digite o {c+1}º número: "))
    s += n
print(f'O somatório de todos é {s}.')
