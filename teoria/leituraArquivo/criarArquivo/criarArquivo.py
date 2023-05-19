# Criar um arquivo
arq = open("arquivoCriado.txt", "x") # Esse comando cria: "x"
arq.write("Danilo Volles Araujo\n") # Escrever
arq.close() # Fechar pra poder ler, se não ele não lê

arq = open("arquivoCriado.txt") # Abrir o arquivo criado
print(arq.read()) # Ler no console

