import jellyfish as jf

comparacao = 'Três Corações'
string = input("Digite a string: ").strip()

levenshtein = jf.levenshtein_distance(string, comparacao)
damerau_levenshtein = jf.damerau_levenshtein_distance(string, comparacao)
jaro = jf.jaro_similarity(string, comparacao)
jaro_winkler = jf.jaro_winkler_similarity(string, comparacao, True)

print('----------------------------------------------')
print('- String:', string)
print('- Comparação:', comparacao)
print('- Tamanho da String:', len(string))
print('----------------------------------------------')

print('Distância de Levenshtein:', levenshtein)
print('Distância de Damerau-Levenshtein:', damerau_levenshtein)
print('Similaridade de Jaro:', jaro)
print('Similaridade de Jaro-Winkler:', jaro_winkler)
