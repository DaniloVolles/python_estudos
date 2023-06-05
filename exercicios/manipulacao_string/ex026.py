# Escreva um programa que leia uma frase inputada pelo usuário e informe:
#     a. Quantas letras 'a' aparecem
#     b. Em que posição ela aparece da primeira vez
#     c. Em que posição ela aparece da ultima vez

string = str(input("Digite uma frase: ")).strip().lower()
print("Existem {} letras 'a' nessa frase.".format(string.count('a')))
print("O primeiro 'a' ocupa a {}a posição na String.".format(string.find('a') + 1))
print("O último 'a' ocupa a {}a posição na String.".format(string.rfind('a') + 1))
