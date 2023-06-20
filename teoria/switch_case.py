frase = input('Digite a sua linguagem de programação: ').upper().strip()

match frase:
    case 'KOTLIN':
        print('Você será um desenvolvedor Mobile')
    case 'JAVA':
        print('Você será um desenvolvedor Back-End')
    case 'JAVASCRIPT':
        print('Você será um desenvolvedor Front-End')
    case 'PYTHON':
        print('Você será um cientista de dados')
    case _:
        print('O importante não é escolher uma linguagem, mas sim, resolver problemas')