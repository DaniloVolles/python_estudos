# Crie um programa que leia o nome completo de uma pessoa e mostre
#   a. O nome com todas as letras maiúsculas
#   b. O nome com todas as letras minúsculas
#   c. Quantas letras ao todo sem considerar espaços
#   d. Quantas letras possui o primeiro nome

nome = str(input("Informe o seu nome completo: ")).strip()
contaLetra = len(nome) - nome.count(' ')
separaPrimeiroNome = nome.find(' ')

print('O nome com todas as letras maiúsculas fica {}.'.format(nome.upper()))
print('O nome com todas as letras minúsculas fica {}.'.format(nome.lower()))
print('O seu nome possui {} letras.'.format(contaLetra))
print('O seu primeiro nome possui {} letras.'.format(separaPrimeiroNome))
