from unidecode import unidecode


def tratar_caracteres_especiais(palavra: str):
    ## Essa função possui 3 partes:
    # 1 - remover caracteres especiais com unidecode_usage
    # 2 - remover ', ´, `,
    # 3 - remover - e _

    # 1 - Isso aqui remove os acentos da palavra -> ç, á, à, ã, ä
    palavra_tratada = unidecode(palavra)

    # 2 - Aqui vamos remover os caracteres especiais -> ', `, ´
    caracteres_1 = "'´`"
    for i in range(0, len(caracteres_1)):
        palavra_tratada = palavra_tratada.replace(caracteres_1[i], '')  # trocar caractere por "backspace"
    # Caracteres ', `, ´ retirados

    # 3 - Aqui vamos remover os caracteres especiais -> -, _,
    caracteres_2 = "-_"
    for i in range(0, len(caracteres_2)):
        palavra_tratada = palavra_tratada.replace(caracteres_2[i], ' ')  # Trocar caractere por "espaço"

    return palavra_tratada


def upper_case_trim(palavra: str):
    return palavra.upper().strip()


nome = "Pingo-d'Água"

print('Nome original:', nome)
print('Nome UpperCase e "stripped":', upper_case_trim(nome))
print('Nome sem caracteres especiais:', tratar_caracteres_especiais(nome))