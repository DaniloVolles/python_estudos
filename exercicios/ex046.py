# Faca um programa que mostre na tela uma contagem regressiva para o Boom, contando de 10 a 0, de 1 em 1 segundo

import time

for c in range(10, 0, -1):
    print(c)
    time.sleep(1.0)
print('BOOOOOOM!!!')
