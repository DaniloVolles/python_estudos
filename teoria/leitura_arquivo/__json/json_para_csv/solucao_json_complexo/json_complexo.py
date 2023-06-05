import json

def export_to_csv():
    with open("arquivo_teste.json") as f: # Abrir arquivo json para leitura
        list1 = [] # Criar a variável do tipo lista. Esta seráimpressa no CSV
        data = json.loads(f.read()) # Carrego na variável 'data' o arquivo json a ser lido
        temp = data['pesssoas'][0] # Variável temporária --> Ela inicia em 0
        header_items = [] # Variável do tipo lista que vai pegar os cabeçalhos
        get_header_items(header_items, temp) # Inicialização do método --> a temp e o header_items como argumentos
        list1.append(header_items) # Escrever linha de cabeçalho

        for obj in data:
            d = [] # Criar uma variável do tipo lista --> ESSA VARIÁVEL INDICA A LINHA DO CSV???
            add_items_to_data(d, obj) # Passar d e obj como argumentos
            list1.append(d) # Colocar a linha na list1

        with open("arquivo_teste.csv", "w") as output_file: # Escrever a list1 no arquivo teste
            for a in list1:
                output_file.write(','.join(map(str, a)) + '\r')


def get_header_items(items, obj): # Esse método 'retorna' os cabeçalhos de todo objeto do json
# ESSA FUNÇÃO SÓ DIZ RESPEITO A CABEÇALHOS
    for x in obj: # Para cada instância desses objetos
        if isinstance(obj[x], dict): # Executar se ele possuir a instancia obj[x] do tipo dicionário
            items.append(x) # Incluir cada item na lista de
            get_header_items(items, obj[x]) # Caso esse "objeto" seja um dicionário, utilizar essa função recursiva no dicionário
        else: # Se não for um dicioário (isinstance), executar o seguinte:
            items.append(x) # incluir o item na lista


def add_items_to_data(items, obj):
# ESSA FUNÇÃO DIZ RESPEITO AOS DADOS QUE SERÃO INCLUIDOS NO CSV
    for x in obj:
        if isinstance(obj[x], dict):
            items.append('')
            get_header_items(items, obj[x])
        else:
            items.append(obj[x])


export_to_csv()
