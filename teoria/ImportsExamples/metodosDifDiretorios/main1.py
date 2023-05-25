from teoria.ImportsExamples.metodosDifDiretorios.function.metodo1 import soma
# Para isso funcionar o programa deve estar organizado em pacotes.
# funcionou.

print("--------------------")
print("Execução do programa")
print("--------------------")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = soma(n1, n2)

print(f"A soma entre {n1} e {n2} é {soma}.")