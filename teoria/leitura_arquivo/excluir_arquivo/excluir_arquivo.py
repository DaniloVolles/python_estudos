import os

# Criar arquivo
arq = open("arquivo.txt", "x")
arq.write("Danilo Volles Araujo\n")

# Fechar arquivo
arq.close()

# Ler arquivo
arq = open("arquivo.txt")
print(arq.read())

# Fechar arquivo
arq.close()

# EXCLUIR ARQUIVO
os.remove("arquivo.txt")
