arq = open("exemplo.txt")
print(arq.read())
print("arquivo fechado? -->", arq.closed)
# Para fechar arquivo utilizar o comando a seguir
arq.close()
print("arquivo fechado? -->", arq.closed)
