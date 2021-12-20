# Recebe uma lista de mensagens e um dicionário
# Verifica se todas as palavras da mensagem estão no dicionário.
# O vetor tipo contém o que vai ser usado: 1 - Texto, 2 - Titulo, 3 - Autor
# Devolve o vetor com as palavras que não estão no dicionário.
def check_dicio(lista, dicio1, dicio2=None, usar2=False, tipo=None):
    if tipo is None:
        tipo = [1, 2]

    resultado = []

    for current_message in lista:

        texto = current_message.text
        titulo = current_message.title
        autor = current_message.author

        texto = texto.replace('<br>', ' ')

        texto = texto.split()
        titulo = titulo.split()
        autor = autor.split()

        words = []

        if 1 in tipo:  # Incluir texto
            for t in texto:
                words.append(t)

        if 2 in tipo:  # Incluir titulo
            for t in titulo:
                words.append(t)

        if 3 in tipo:  # Incluir autor
            for a in autor:
                words.append(a)

        for current_check in words:

            if not usar2:
                if current_check in dicio1 or current_check.lower() in dicio1:
                    # print("OK: " + str(current_check))
                    a = 8
                else:
                    # print("NOT: " + str(current_check))
                    resultado.append(current_check)
            else:
                if not (
                        current_check in dicio1 or current_check.lower() in dicio1 or current_check in dicio2 or current_check.lower() in dicio2):
                    resultado.append(current_check)
    return resultado


# Recebe uma lista de mensagens, e conta quantas palavras há em cada  mensagem.
# Pode contar texto (1), título (2) ou autor (3).
# Devolve um vetor com cada contagem realizada, pra cada mensagem
def num_palavras(lista, tipo=1):
    num_palavras_msg_serie = []

    for current_message in lista:
        if tipo == 1:
            texto = current_message.text
        elif tipo == 2:
            texto = current_message.title
        else:
            texto = current_message.author

        texto = texto.replace('<br>', ' ')
        words = texto.split()

        number_of_words = len(words)
        # print([item for item, count in collections.Counter(words).items() if count > 1])
        num_palavras_msg_serie.append(number_of_words)

    return num_palavras_msg_serie


# Recebe uma lista de mensagens, e conta quantas palavras há em cada linha.
# Devolve um vetor com cada contagem realizada, por cada linha.
def num_palavras_linha(lista):
    num_palavras_linha_serie = []

    for current_message in lista:

        current_line = current_message.text
        number_of_lines = current_line.count('<br>') + 1

        for i in range(number_of_lines):
            count_words = current_line.partition('<br>')[0]
            current_line = current_line.partition('<br>')[2]

            word_list = count_words.split()
            number_of_words = len(word_list)
            num_palavras_linha_serie.append(number_of_words)

    return num_palavras_linha_serie


# Recebe uma lista de mensagens, e conta quantas letras há em cada linha.
# Devolve um vetor com cada contagem realizada, por cada linha.
def num_letras_linha(lista):
    letras_linha_serie = []

    for current_message in lista:

        current_line = current_message.text
        number_of_lines = current_line.count(' <br> ') + 1

        for i in range(number_of_lines):
            count_words = current_line.partition(' <br> ')[0]
            current_line = current_line.partition(' <br> ')[2]

            number_of_letters = len(count_words)

            letras_linha_serie.append(number_of_letters)
            if number_of_letters > 70:
                current_message.print()

    return letras_linha_serie


# Recebe uma lista de mensagens, e conta quantas linhas há em cada texto.
# Devolve um vetor com cada contagem realizada, por cada linha.
def num_linhas(lista):
    linhas_serie = []

    for current_message in lista:
        # Contar linhas
        texto = current_message.text
        number_of_lines = texto.count('<br>') + 1
        linhas_serie.append(number_of_lines)  # Há sempre uma linha a mais do que o número de <br>s.
        if number_of_lines == 8:
            current_message.print()

    return linhas_serie


# Produz um vetor com o número de palavras em cada frequência.
# Devolve o vetor com o valor de cada palavra, sem nome, pronto para ser
# convertido em histograma.
def freq_palavras(lista, tipo = 1):
    wordfreq = {}
    for current_message in lista:
        if tipo == 1:
            texto = current_message.text
        elif tipo == 2:
            texto = current_message.title
        else:
            texto = current_message.author

        texto = texto.replace('<br>', ' ')
        words = texto.split()
        for raw_word in words:
            if raw_word not in wordfreq:
                wordfreq[raw_word] = 0
            wordfreq[raw_word] += 1

    sort = sorted(wordfreq.items(), key=lambda item: item[1], reverse=True)

    hist = []

    for i in sort:
        hist.append(int(i[1]))
    return hist

# Recebe as mensagens.
# Calcula as letras mais frequentes no texto (1), títulos (2) e autores (3).
# Devolve um dicionário.
def freq_letras(lista, tipo = 1):
    charfreq = {}
    for current_message in lista:
        if tipo == 1:
            texto = current_message.text
        elif tipo == 2:
            texto = current_message.title
        else:
            texto = current_message.author

        texto = texto.replace('<br>', ' ')
        texto = texto.replace(' ', '')
        texto = texto.lower()
        for char in texto:
            if char not in charfreq:
                charfreq[char] = 0
            charfreq[char] += 1

    sort = sorted(charfreq.items(), key=lambda item: item[1], reverse=True)

    true_dict = {}
    for i in range(len(sort)):
        true_dict[sort[i][0]] = sort[i][1]

    return true_dict


# Recebe as mensagens e o valor de n.
# Calcula as n-esimas letras mais frequentes nas linhas.
# Devolve um dicionário.
def freq_nesimas_letras_linhas_palavras(lista, n, m = 9999):
    charfreq = {}

    for current_message in lista:

        current_line = current_message.text
        current_line = current_line.lower()
        number_of_lines = current_line.count(' <br> ') + 1

        for i in range(number_of_lines):
            analysis_line = current_line.partition(' <br> ')[0]
            current_line = current_line.partition(' <br> ')[2]
            try:
                if m != 9999:
                    linha_cortada = analysis_line.split()
                    linha_cortada = linha_cortada[m-1]
                else:
                    linha_cortada = analysis_line
                char = linha_cortada[n-1]

                '''
                print(analysis_line)
                print("Pegando: " + linha_cortada)
                print("Pegando: " + char)
                print("-----------------")
                '''

                if char not in charfreq:
                    charfreq[char] = 0
                charfreq[char] += 1
            except:
                pass
    sort = sorted(charfreq.items(), key=lambda item: item[1], reverse=True)

    true_dict = {}
    for i in range(len(sort)):
        true_dict[sort[i][0]] = sort[i][1]

    return true_dict

# Recebe as mensagens e o valor de n.
# Calcula as n-esimas letras mais frequentes nas linhas.
# Devolve um dicionário.
def freq_nesimas_letras_linhas_titulos(lista, n, m = 9999):
    charfreq = {}

    for current_message in lista:

        current_line = current_message.title
        current_line = current_line.lower()

        for i in range(1):
            try:
                if m != 9999:
                    linha_cortada = current_line.split()
                    linha_cortada = linha_cortada[m-1]
                else:
                    linha_cortada = current_line
                char = linha_cortada[n-1]

                #print(current_line)
                #print("n = " + str(n) + "e m = " + str(m))
                #print("Pegando: " + linha_cortada)
                #print("Pegando: " + char)
                #print("-----------------")

                if char not in charfreq:
                    charfreq[char] = 0
                charfreq[char] += 1
            except:
                pass
    sort = sorted(charfreq.items(), key=lambda item: item[1], reverse=True)

    true_dict = {}
    for i in range(len(sort)):
        true_dict[sort[i][0]] = sort[i][1]

    return true_dict


