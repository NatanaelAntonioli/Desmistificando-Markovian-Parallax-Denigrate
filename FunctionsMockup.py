from classMessage import *
from random import randint


# Produz um conjunto de mensagens na forma de um mockup.
# É feito a partir de dois dicionários, um para nomes e um para texto e autor.
# O algoritmo daqui está descrito no desmistificando.
def load_mockup(dicio, dicionomes, total=618):
    mensagens = []

    for i in range(total):

        # Cria o título
        total_palavras_titulo = randint(1, 3)
        titulo = ''

        for j in range(total_palavras_titulo):
            random_word_index = randint(0, len(dicio) - 1)
            titulo = titulo + dicio[random_word_index].capitalize() + ' '

        # Cria o autor
        autor = ''
        guia_autor = randint(1, 5)
        if guia_autor == 1:
            random_word_index = randint(0, len(dicionomes) - 1)
            autor = autor + dicionomes[random_word_index].capitalize() + ' '
        else:
            for k in range(2):
                random_word_index = randint(0, len(dicio) - 1)
                autor = autor + dicio[random_word_index].capitalize() + ' '

        # Cria o texto
        # Determina quantas linhas a mensagem terá.
        guia_linhas1 = randint(0, 90)

        if guia_linhas1 < 5:
            total_linhas = 3
        elif guia_linhas1 < 30:
            total_linhas = 4
        elif guia_linhas1 < 55:
            total_linhas = 5
        elif guia_linhas1 < 80:
            total_linhas = 6
        else:
            total_linhas = 7

        texto = ''

        for L in range(total_linhas):
            texto_line = ''

            while True:

                random_word_index = randint(0, len(dicio) - 1)
                candidato = texto_line + dicio[random_word_index] + ' '

                test = candidato.replace('<br>', '')
                test = test.replace(' <br>', '')

                if len(test) > 71:
                    break
                else:
                    texto_line = texto_line + dicio[random_word_index] + ' '

            if L < total_linhas - 1:
                texto = texto + texto_line + '<br> '
            else:
                texto = texto + texto_line
                texto = texto[:-1]

        novo = Message("Mensagem " + str(i+1), autor, titulo, texto)
        mensagens.append(novo)

    return mensagens
