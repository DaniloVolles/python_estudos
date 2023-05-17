nome = "Danilo Volles Araujo"
nome2 = "         Andressa Adelaide            "
string = "curso de python com gustavo guanabara"

# FATIAMENTO DE STRING
type(str)
print(nome[3]) #Começa em 0
print(nome[3:6])
print(nome[3:12:2]) #Pula caracteres de dois em dois
print(nome[:13]) #Começa a contagem em 0, quando se omite a parte antes do ":"
print(nome[2::3]) #Começa no 2, vai até o final e pula de 3 em 3

# ANÁLISE DE STRING
print(len(nome)) #Qual o comprimento dessa string?
print(nome.count('o')) #contar quantos 'o' aparecem (Case Sensitive)
print(nome.count('o', 0, 13)) #contar quantos 'o' aparecem entre 0 e 13
print(nome.find('lles')) # Conta quantos caracteres aparecem até encontrar o "lles"
print('Volles' in nome) # Existe a cadeia "Volles" em nome?

# TRANSFORMAÇÕES NA STRING
nomeReplace = nome.replace('Araujo', 'Fedrigo')
print(nomeReplace)
print(nome)

print(nome.upper()) # Coloca a String em maiúsculas
print(nome.lower()) # Coloca a String em minúsculas
print(nome.capitalize()) # Coloca apenas a primeira letra da String em maiúsculo
print(nome.title()) # Coloca a String em minúsculas
print(string.title()) # Palavras de 1 ou 2 letras/caracteres, também

print(nome2.strip()) # Remove espaços excedentes no início e no final da string
print(nome2.rstrip()) # Right / Direita
print(nome2.lstrip()) # Left / Esguerda

# DIVISÃO DE STRING
lista = nome.split()
lista2 = nome2.split()

print(lista) # Forma uma lista com todas as palavras da String
print(lista2) # Essa função já tem um strip inerente

# JUNÇÃO DE STRING
print('-'.join(lista)) # Essa função junta as palavras da lista utilizando o que está dentro de ''.
