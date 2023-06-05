# Criar um arquivo
arq = open("arquivo_criado.txt", "x") # Esse comando cria: "x"
arq.write("Danilo Volles Araujo\n") # Escrever
arq.close() # Fechar pra poder ler, se não ele não lê

arq = open("arquivo_criado.txt") # Abrir o arquivo criado
print(arq.read()) # Ler no console

