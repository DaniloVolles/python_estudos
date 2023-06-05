# Escreva um programa que leia o nome de uma cidade e diga se começa com a palavra "Santo"

cidade = str(input('Digite o nome da cidade: ')).strip().upper() # Elimina espaços antes e após ao digitar e transforma tudo em maiúsculo.
comecaSanto = cidade.find('SANTO') == 0 ## comecaSanto é um booleano
print(comecaSanto) # Retorna true ou false
