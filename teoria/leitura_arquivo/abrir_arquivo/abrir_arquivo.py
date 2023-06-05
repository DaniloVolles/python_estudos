# Abrir (arquivo.txt, modo de abertura)
arq1 = open("arquivo01.txt", "rt")
arq2 = open("arquivo02.txt")
arq3 = open("arquivo03.txt")

print(arq1.mode, "--> esse é o modo de abertura do arquivo --> arq1.mode")
print(arq1.name, "--> esse é o nome do arquivo --> arq1.name")
print(arq1.closed, "--> esse é o status de abertura do arquivo --> arq1.closed (fechado - true, aberto - false)")

# Modos de abrir o arquivo:
'''
    (É o 2ºargumento)
    "rt" por default

    modo:
    "r" -- read
    "a" -- append
    "w" -- write
    "x" -- create

    forma de leitura:
    "t" -- text
    "b" -- binaries
'''
