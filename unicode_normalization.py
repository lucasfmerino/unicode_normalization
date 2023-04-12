"""
# unicodedata
    text_2 = unicodedata.normalize("NFD", text)
    print(text_2)  # ex: vários último peça

    text_2 = text_2.encode("ascii", "ignore")
    print(text_2)  # ex: b' varios ultimo peca'

    text_2 = text_2.decode("utf-8")
    print(text_2)  # ex: varios ultimo peca

"""

import unicodedata


def unicode_normalization(string):
    text = unicodedata.normalize("NFD", string)
    text = text.encode("ascii", "ignore")
    text = text.decode("utf-8")
    return text


if __name__ == "__main__":

    text = input("Insira a string que deseja normalizar: ")
    print()

    text_n = unicode_normalization(text)
    print(text_n)
