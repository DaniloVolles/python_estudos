# Faça um programa que leia o nome completo de uma pessoa
#     a. Esse programa deve mostrar o primeiro e o ultimo nome separadamente

nome = str(input('Digite o seu nome completo: ')).strip().split() # Aqui já transforma em lista
print(f'Primeiro nome: {nome[0]}.')
print(f'Último nome: {nome[-1]}.') # Aqui você força o programa a contar de trás pra frente

# Utilizando a função 'len'
print(f'Último nome: {nome[len(nome)-1]}.') # Como inicia em 0, tem que por o -1
