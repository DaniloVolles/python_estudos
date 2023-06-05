#O python tem 4 tipos primitivos: int, float, bool, str

n1 = input('Digite o 1o numero: ')
n2 = input('Digite o 2o numero: ')
s = n1 + n2
print('A soma entre {} e {} é {}.'.format(n1, n2, s))

print('Por default esses inputs são realizados como strings, é preciso forçar o programa a aceitar um int')

# Perceba o "int()" antes do "input()"
n3 = int(input("Digite o 3o número: "))
n4 = int(input("Digite o 4o número: "))

s2 = n3 + n4
print('A soma entre {} e {} é {}.'.format(n3, n4, s2))

# O mesmo vale para bool, float e str

nome = str(input('Digite o seu nome: ')) # Por default já é string, então não faz diferença
print(nome)
print(type(nome))
booleano = bool(input('Digite [True/False]: '))
print(booleano)
print(type(booleano))
nFlutuante = float(input('Digite os 5 primeiros dígitos de Pi: '))
print(nFlutuante)
print(type(nFlutuante))