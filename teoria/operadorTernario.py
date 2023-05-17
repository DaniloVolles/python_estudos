# Python não tem Operador Ternário, mas tem um if simplificado assim como o Kotlin

idade = int(input("Quantos anos você tem? "))
print('Adulto' if idade >= 18 else 'Criança')

# O mesmo programa poderia ser escrito assim:
if idade >= 18:
    print('Adulto')
else:
    print('Criança')
