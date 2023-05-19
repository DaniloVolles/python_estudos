import os

def criar(nomeArquivo):
    arq = open(nomeArquivo, "x")
    arq.close()

def escrever(nomeArquivo):
    arq = open(nomeArquivo, "r+")
    escrita = str(input("Digite a sua mensagem: "))
    arq.write(escrita)
    arq.close()

def ler(nomeArquivo):
    arq = open(nomeArquivo)
    print(arq.read())
    arq.close()

def excluir(nomeArquivo):
    os.remove(nomeArquivo)

print("Seja bem vindo ao sistema de criação e gerenciamento de arquivos!")
print("Por favor, digite a ação desejada: ")
print("1 --> Criar um arquivo.\n"
      "2 --> Escrever em um arquivo.\n"
      "3 --> Ler um arquivo.\n"
      "4 --> Excluir um arquivo.")

opcao = int(input("Opção: "))
nomeArquivo = str(input("Digite o nome do arquivo em questão: "))+".txt"

if opcao == 1:
    criar(nomeArquivo)
elif opcao == 2:
    escrever(nomeArquivo)
elif opcao == 3:
    ler(nomeArquivo)
elif opcao == 4:
    excluir(nomeArquivo)
else:
    print("Digite novamente: ")
