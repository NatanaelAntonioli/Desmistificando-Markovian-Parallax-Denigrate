import json
from classMessage import *
import matplotlib.pyplot as plt


# A partir de um histograma original (barras vermelhas), produz um
# gráfico de barras com intervalos de controle (média, máximos e mínimos em azul)
# Em um dado intervalo e com dadas legendas.
# Exibe gráfico. Não retorna nada.
def make_bar_comp_plot(original, histogramas_controle, minimo, maximo, eixoX="X-Label", eixoY="Y-Label"):

    means = find_mean(histogramas_controle)
    vector_min = get_max_min(histogramas_controle, 1)
    vector_max = get_max_min(histogramas_controle, 2)

    x_main = []
    y_main = []
    y_means = []
    y_max = []
    y_min = []
    errors = []
    centers = []
    for i in range(maximo - minimo):
        x_main.append(str(i + minimo))
        y_main.append(original[i + minimo])
        y_means.append(means[i + minimo])
        y_min.append(vector_min[i + minimo])
        y_max.append(vector_max[i + minimo])
        errors.append((vector_max[i + minimo] - vector_min[i + minimo]) / 2)
        centers.append(vector_min[i + minimo] + (vector_max[i + minimo] - vector_min[i + minimo]) / 2)

    # creating the bar plot
    plt.bar(x_main, y_main, color='maroon', width=0.8)
    plt.bar(x_main, centers, yerr=errors, color='green', width=0,
            error_kw=dict(ecolor='blue', lw=0.8, capsize=5, capthick=0.8))
    plt.plot(x_main, y_means, marker=".", linestyle="", alpha=1, color="b")

    xlocs, xlabs = plt.xticks()
    plt.xlabel(eixoX)
    plt.ylabel(eixoY)
    plt.show()


# Recebe um vetor de ocorrências
# Conta quantas ocorrências tem em outro vetor.
# O elemento i do vetor indica quantas ocorrências existem de i coisas.
# Devolve o vetor histograma.
def get_histogram(vector, max):
    hist = [0 for i in range(max)]
    for i in vector:
        hist[i] = hist[i] + 1

    return hist


# Recebe um vetor de histogramas.
# Devolve um vetor de mínimos (1) ou máximos (2) nesses histogramas.
def get_max_min(array, objetivo):
    tam = len(array[0])
    if objetivo == 1:
        out = [99999999999999 for i in range(tam)]
    else:
        out = [-99999999999999 for i in range(tam)]
    for hist in array:
        counter = 0
        for j in hist:
            if objetivo == 1:
                if j < out[counter]:
                    out[counter] = j
            else:
                if j > out[counter]:
                    out[counter] = j
            counter = counter + 1

    return out


# Recebe um vetor de dicionários.
# Devolve um dicionários de mínimos (1) ou máximos (2).
def get_max_min_dict(array, original, tipo):
    tam = len(array)
    # Primeiro, preenche o vetor de médias vazio.

    extrem_dics = {}
    for letter in original:
        if tipo == 1:
            extrem_dics[letter] = 99999999999999
        else:
            extrem_dics[letter] = -99999999999999
    #print(extrem_dics)

    # Agora, somamos
    for hist in array: # Para cada dicionário do array de dicionários
        for letter in extrem_dics: # Para cada letra do dicionário final
            try:
                if tipo == 1:
                    if hist.get(str(letter)) < extrem_dics[str(letter)]:
                        extrem_dics[str(letter)] = hist.get(str(letter))
                else:
                    if hist.get(str(letter)) > extrem_dics[str(letter)]:
                        extrem_dics[str(letter)] = hist.get(str(letter))
            except:
                b = 9
    return extrem_dics


# Calcula a média de um vetor de histogramas.
# Devolve o vetor com as médias
def find_mean(array):
    tam = len(array)
    #print("Divindo por: " + str(tam))
    mean = [0 for i in range(tam)]
    for hist in array:
        counter = 0
        for j in hist:
            mean[counter] = mean[counter] + j
            counter = counter + 1

    for k in range(len(mean)):
        mean[k] = mean[k] / tam

    return mean


# Calcula a média de um vetor de dicionários.
# Devolve o dicionário com as médias
def find_mean_dict(array, original):
    tam = len(array)

    # Primeiro, preenche o vetor de médias vazio.

    means_dics = {}
    for letter in original:
        means_dics[letter] = 0
    #print(means_dics)

    # Agora, somamos
    for hist in array: # Para cada dicionário do array de dicionários
        for letter in means_dics: # Para cada letra do dicionário final
            try:
                means_dics[str(letter)] = means_dics[str(letter)] + hist.get(str(letter))
            except:
                b = 9

    for letter in original:
        means_dics[letter] = means_dics[letter]/tam

    return means_dics


# Calcula o vetor de desvios padrões.
# Recebe o vetor de médias e o vetor de histogramas.
def find_sd(mean, array):
    tam = len(array[0])
    sd = [0 for i in range(tam)]

    for hist in array:
        counter = 0
        for j in hist:
            sd[counter] = sd[counter] + (j - mean[counter]) ** 2
            counter = counter + 1

        for k in range(len(mean)):
            sd[k] = sd[k] / tam
            sd[k] = sd[k] ** 0.5

    return sd


# Carrega os dados nos arquivos .json em objetos do tipo Message.
# Devolve uma lista de objetos do tipo Message.
def load_objects():
    with open("texts.json", 'r') as te:
        texts = json.load(te)

    with open("titles.json", 'r') as tl:
        titles = json.load(tl)

    with open("authors.json", 'r') as a:
        authors = json.load(a)

    with open("filenames.json", 'r') as f:
        filenames = json.load(f)

    messages = []

    ## Cria nossa lista de palavras

    for i in range(len(authors)):
        # def __init__(self, file, author, title, text):
        sanitizedText = texts[i].replace('&#39;', "'")
        sanitizedText = sanitizedText.replace('&amp;', "&")
        sanitizedText = sanitizedText.replace('<br>', " <br> ")

        sanitizedTitle = titles[i].replace('&#39;', "'")
        sanitizedTitle = sanitizedTitle.replace('&amp;', "&")
        sanitizedTitle = sanitizedTitle.replace('<br>', " <br> ")

        sanitizedAuthor = authors[i].replace('&#39;', "'")
        sanitizedAutor = sanitizedAuthor.replace('&amp;', "&")
        sanitizedAutor = sanitizedAuthor.replace('<br>', " <br> ")

        new_message = Message(filenames[i], sanitizedAuthor, sanitizedTitle, sanitizedText)

        messages.append(new_message)

    return messages


# Carrega a lista de palavras especificada no arquivo.
# A definimos como a lista mais provável para a origem do texto.
# Devolve um vetor de palavras.
def load_dicio(file):
    dicio = []
    file1 = open(file, 'r')
    Lines = file1.readlines()
    for line in Lines:
        sanitezed = line.replace('\n', '')
        sanitezed = sanitezed.split("/", 1)[0]
        dicio.append(sanitezed)

    return dicio


# Imprime todas as mensagens.
# Não devolve nada.
def print_all(mensagens):
    for current in mensagens:
        current.print()

# Faz um gráfico no qual o eixo X possui categorias ao invés de número.
# Não devolve nada.
def make_label_bar_plot(dic_original, dic_mean, dic_min, dic_max, eixoX="X-Label", eixoY="Y-Label"):
    keys = dic_original.keys()
    values = dic_original.values()
    means = dic_mean.values()
    mins = dic_min.values()
    maxs = dic_max.values()

    x_main = []
    y_main = []
    y_means = []
    y_max = []
    y_min = []
    centers = []
    errors = []
    for i in keys:
        x_main.append(i)

    for j in values:
        y_main.append(j)

    for k in means:
        y_means.append(k)

    for l in maxs:
        y_max.append(l)

    for m in mins:
        y_min.append(m)

    for n in range(len(maxs)):
        centers.append(y_min[n] + (y_max[n] - y_min[n]) / 2)

    for p in range(len(maxs)):
        errors.append((y_max[p] - y_min[p])/2)

    plt.bar(x_main, y_main, color='maroon', width=0.8)
    plt.plot(x_main, y_means, marker=".", linestyle="", alpha=1, color="b")
    plt.bar(x_main, centers, yerr=errors, color='green', width=0,
            error_kw=dict(ecolor='blue', lw=0.8, capsize=5, capthick=0.8))


    plt.xlabel(eixoX)
    plt.ylabel(eixoY)
    plt.show()

# De um dicionário, conta quantos valores são outliers ( < min ou > max).
def count_outliers(dic_original, dic_mean, dic_min, dic_max):
    outliers = 0

    keys = dic_original.keys()
    values = dic_original.values()
    means = dic_mean.values()
    mins = dic_min.values()
    maxs = dic_max.values()

    x_main = []
    y_main = []
    y_means = []
    y_max = []
    y_min = []

    for i in keys:
        x_main.append(i)

    for j in values:
        y_main.append(j)

    for k in means:
        y_means.append(k)

    for l in maxs:
        y_max.append(l)

    for m in mins:
        y_min.append(m)

    counter = 0
    for v in y_main:
        if v < y_min[counter] or v > y_max[counter]:
            outliers = outliers + 1
            #print("Outlier: " + str(y_min[counter]) + "-" + str(v) + "-" + str(y_max[counter]))
        counter = counter + 1

    #print("Returning: " + str(outliers))
    return outliers