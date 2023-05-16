# Crie um programa que avalie um texto transformando ele em maiúsculas, minusculas e dizendo quantas letras possui

nome = str(input("Digite o seu nome completo: ")).strip() ## strip elimina os espaços entre, antes e após letras
print("Analisando o seu nome...")
print("Seu nome em maiúsculas é: {}.".format(nome.upper()))
print("Seu nome em minúsculas é: {}.".format(nome.lower()))
print("Seu nome completo tem {} letras.".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras.".format(nome.find(" ")))
