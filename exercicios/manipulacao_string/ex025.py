# Escrever programa que informe se a pessoa possui 'Silva' no nome

nome = str(input("Digite o seu nome completo: ")).strip().lower()
possuiSilva = "silva" in nome
print(possuiSilva)
