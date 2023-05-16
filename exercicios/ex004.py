# Escreva um programa que diga diversas informações sobre uma variável

variavel = input("Digite algo: ")

print('Contem letras ou números?', variavel.isalnum())
print('Contem apenas letras?', variavel.isalpha())
print('Tipo primitivo dessa variável:', type(variavel))
print('Contem apenas números?', variavel.isdigit())
print('Está em minúsculas?', variavel.islower())
