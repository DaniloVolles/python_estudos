import jellyfish as jf

comparacao = "Massaranduba"
string = input("Digite a string: ").strip()

# Comparação de String
levenshtein = jf.levenshtein_distance(string, comparacao)
damerau_levenshtein = jf.damerau_levenshtein_distance(string, comparacao)
jaro = jf.jaro_similarity(string, comparacao)
jaro_winkler = jf.jaro_winkler_similarity(string, comparacao, True)
match_rating_approach_comparisson = jf.match_rating_comparison(string, comparacao)

# Comparação Fonética
match_rating_codex_string = jf.match_rating_codex(string)
match_rating_codex_comparacao = jf.match_rating_codex(comparacao)

metaphone_string = jf.metaphone(string)
metaphone_comparacao = jf.metaphone(comparacao)

nysiis_string = jf.nysiis(string)
nysiis_comparacao = jf.nysiis(comparacao)

american_soundex_string = jf.soundex(string)
american_soundex_comparacao = jf.soundex(comparacao)

print('----------------------------------------------')
print('- String:', string)
print('- Comparação:', comparacao)
print('- Tamanho da String:', len(string))
print('----------------------------------------------')
print('- As strings são iguais:', string == comparacao)
print('----------------------------------------------')

print('\n------------------------ Comparações de String\n')
print('Distância de Levenshtein:', levenshtein)
print('Distância de Damerau-Levenshtein:', damerau_levenshtein)
print('Similaridade de Jaro:', jaro)
print('Similaridade de Jaro-Winkler:', jaro_winkler)
print('Match Rating Approach:', match_rating_approach_comparisson)

print('\n------------------------ Comparações Fonéticas')

print('\nMatch Rating Codex ---------------------------')
print('----- String:', match_rating_codex_string)
print('----- Comparação:', match_rating_codex_comparacao)
print('----- São iguais?', match_rating_codex_string == match_rating_codex_comparacao)

print('\nMetaphone ------------------------------------')
print('----- String:', metaphone_string)
print('----- Comparação:', metaphone_comparacao)
print('----- São iguais?', metaphone_string == metaphone_comparacao)

print('\nNYSIIS ---------------------------------------')
print('----- String:', nysiis_string)
print('----- Comparação:', nysiis_comparacao)
print('----- São iguais?', nysiis_string == nysiis_comparacao)

print('\nAmerican Soundex -----------------------------')
print('----- String:', american_soundex_string)
print('----- Comparação:', american_soundex_comparacao)
print('----- São iguais?', american_soundex_string == american_soundex_comparacao)