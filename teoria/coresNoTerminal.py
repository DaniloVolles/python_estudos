# Como colocar cores no terminal?

idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print('\033[7;34mAdulto\033[m')
    print('\033[34mAdulto\033[m')
else:
    print('\033[7;31mCriança\033[m')
    print('\033[31mCriança\033[m')
    # print('\033[7;31;42mCriança\033[m') #Possibilidade com 3 argumentos

a = 2
b = 5
print(f'Os valores são \033[34m{a}\033[m e \033[31m{b}\033[m!')

# Facilitando:
cores = {'limpa': '\033[m',
         'v': '\033[31m',
         'a': '\33[33m'}

print('Os valores são {}{}{} e {}{}{}!'.format(
    cores['v'], a, cores['limpa'],
    cores['a'], b, cores['limpa']
))

""" 
Padrão ANSI

\033['num para estilo';'3num para cor do texto';'3num para fundo'm
exs.: \033[0;33;44m
   .: \033[7;32;47m

estilo: (primeiro número após colchetes)
0 -> none
1 -> bold
4 -> underline
7 -> negative

cor: (segundo número após colchetes)
30 -> branco
31 -> vermelho
32 -> verde
33 -> amarelo
34 -> azul
35 -> roxo
36 -> ciano
37 -> cinza

cor de fundo: (terceiro número após colchetes)
40 -> branco
41 -> vermelho
42 -> verde
43 -> amarelo
44 -> azul
45 -> roxo
46 -> ciano
47 -> cinza
"""
