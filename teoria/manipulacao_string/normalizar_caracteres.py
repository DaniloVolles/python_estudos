import pandas as pd
import unicodedata

def remover_acentos(string):
    # Remove acentos das palavras.

    ajuste = string.upper()
    ajuste = unicodedata.normalize("NFD", string).encode("ASCII", "ignore").decode("utf-8")

    return ajuste

string = 'Á, À, Ã, Â, Ä, Ç, Ü'
string = remover_acentos(string)
print(string)