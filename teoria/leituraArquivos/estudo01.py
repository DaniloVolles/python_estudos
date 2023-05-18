# Modos de abrir o arquivo:
'''
    (É o 2ºargumento)
    "rt" por default

    modo:
    "r" -- read
    "a" -- add
    "w" -- write
    "x" -- create

    forma de leitura:
    "t" -- text
    "b" -- binaries
'''

# Abrir (arquivo.txt, modo de abertura)
str1 = open("arquivo01.txt", "rt")
str2 = open("arquivo02.txt")
str3 = open("arquivo03.txt")

print(str1.mode, "--> esse é o modo de abertura do arquivo --> str1.mode")
print(str1.name, "--> esse é o nome do arquivo --> str1.name")
print(str1.closed, "--> esse é o status de abertura do arquivo --> str1.closed (fechado - true, aberto - false)")

print(str2.read()) # Dá pra ler tudo de uma vez

print(str1.read(12)) # Dá pra passar um int como argumento para read informando quantos bytes devem ser lidos
print(str1.read()) # Aqui ele lê o resto

print(type(str2.read())) # O tipo é uma string

# Para fechar um arquivo e poder utilizar os outros recursos relacionados a ele:
str1.close()
print(str1.closed) # Retorna true, pois o fechamos
print(str2.closed) # Retorna false, pois não o fechamos

# Para ler apenas uma linha, utilizar readline(), para ler todas as linhas, utilizar readlines()
print(str3.readline())
print(str3.readlines())
str3.close()
str3 = open("arquivo03.txt")

#Em um laço de repetição
# for line in str3:
#     print(read())
