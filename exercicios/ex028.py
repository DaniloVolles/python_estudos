# Crie um jogo de adivinhação, em que o computador 'pensa'
# em um número e a gente tenta adivinhar o número que o computador pensou

from random import randint
computador = randint(1, 5)

aposta = int(input('Qual foi o número entre 1 e 5 que eu pensei? '))
if aposta == computador:
    print(f'Parabéns, você GANHOU, o número que eu pensei foi o {aposta}.')
else:
    print(f'Não foi dessa vez, você PERDEU, o número que eu pensei foi o {computador}.')
