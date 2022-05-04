from readchar import readchar
import os

traducoes = {
    ' ': ' / ',
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.--',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'

}

palavra_digitada = ""

traduzido = []

print('-=' * 78)
print('CONVERSOR DE CÓDIGO MORSE'.center(162))
print('-=' * 78)

print("Frase digitada: ", end='')
while True:
    palavra = readchar().decode().lower()
    os.system('cls')
    print("Frase digitada: ", end='')
    if palavra == '\x08':
        if len(traduzido) == 0:
            pass
        else:
            palavra_digitada = palavra_digitada[:len(palavra_digitada)-1]
            traduzido.pop()
        print(palavra_digitada)
        print()
        print('-=' * 81)
        print()
    else:
        palavra_digitada += palavra
        print(palavra_digitada)
        print()
        print('-=' * 81)
        print()

        for letra in palavra:
            traduzido.append(traducoes[str(letra)])
    print('Tradução em código-morse: ', end='')
    for char in traduzido:
        print(char, end=' ')

