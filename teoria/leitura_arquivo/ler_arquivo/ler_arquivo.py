arq1 = open("arquivo1.txt")
arq2 = open("arquivo2.txt")
arq3 = open("arquivo3.txt")

# Leitura do arquivo
print(arq2.read()) # Dá pra ler tudo de uma vez

print(arq1.read(12)) # Dá pra passar um int como argumento para read informando quantos bytes devem ser lidos
print(arq1.read()) # Aqui ele lê o resto

print(type(arq2.read())) # O tipo é uma string

# Para fechar um arquivo e poder utilizar os outros recursos relacionados a ele:
arq1.close()
print(arq1.closed) # Retorna true, pois o fechamos
print(arq2.closed) # Retorna false, pois não o fechamos

# Para ler apenas uma linha, utilizar readline(), para ler todas as linhas, utilizar readlines()
print(arq3.readline())
print(arq3.readlines())
arq3.close()

arq3 = open("arquivo3.txt")

#Em um laço de repetição
for line in arq3.readlines():
    print('oi') #Aqui é um print, mas vc pode fazer o que vc quiser com cada linha
arq3.close()


# Modos de abrir o arquivo:
'''
    (É o 2ºargumento)
    "rt" por default

    modo:
    "r" -- read
    "a-- write
    "x" -" -- append
    "w" - create

    forma de leitura:
    "t" -- text
    "b" -- binaries
'''
