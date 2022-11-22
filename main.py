
from random import choice


with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

palavra = choice(lista_de_palavras).upper()

forca = """
____
    |
    |
    -"""

vazio = """


"""
cabeca = """
    O

"""
tronco = """
    O
    |
"""
braco_esquerdo = """
    O
   /|
"""
braco_direito = """
    O
   /|\\
"""
perna_esquerda = """
    O
   /|\\
   /
"""
perna_direita = """
    O
   /|\\
   / \\
"""

chances_do_boneco = [
    vazio,
    cabeca,
    tronco,
    braco_esquerdo,
    braco_direito,
    perna_esquerda,
    perna_direita,
]

acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''

while acertos != len(palavra) and erros != 7:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += f'{letra} '
        else:
            mensagem += '_ '
    print(forca+chances_do_boneco[erros])
    print(mensagem)

    
    letra = input('Digite a letra: ').upper()
    
    if letra in letras_acertadas+letras_erradas:
        print('Você já tentou essa letra')
        continue

    if letra in palavra:
        print('Você acertou a letra')
        letras_acertadas += letra
        acertos += palavra.count(letra)
    else:
        print('Você errou a letra')
        letras_erradas += letra
        erros += 1