# Importações necessárias

from classMessage import *
from FunctionsBase import *
from FunctionsDescritivas import *
from FunctionsMockup import *

from tabulate import tabulate
import collections


# Compara o total de palavras em cada mensagem (1), título (2) ou autor(3).
def compare_num_palavras(lista, dicio, trials, tipo):
    original_occ = num_palavras(lista, tipo)
    original_hist = get_histogram(original_occ, 100)

    histogramas_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_occ = num_palavras(current_mockup, tipo)
        mockup_hist = get_histogram(mockup_occ, 100)
        histogramas_controle.append(mockup_hist)

    if tipo == 1:
        make_bar_comp_plot(original_hist, histogramas_controle, 20, 70, "Número de palavras na mensagem",
                           "Número de mensagens")
    elif tipo == 2:
        make_bar_comp_plot(original_hist, histogramas_controle, 0, 5, "Número de palavras no título",
                           "Número de mensagens")
    else:
        make_bar_comp_plot(original_hist, histogramas_controle, 0, 5, "Número de palavras no autor",
                           "Número de mensagens")


# Compara o total de palavras na linha do texto.
def compare_num_palavras_linhas(lista, dicio, trials):
    original_occ = num_palavras_linha(lista)
    original_hist = get_histogram(original_occ, 100)

    histogramas_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_occ = num_palavras_linha(current_mockup)
        mockup_hist = get_histogram(mockup_occ, 100)
        histogramas_controle.append(mockup_hist)

    make_bar_comp_plot(original_hist, histogramas_controle, 4, 14, "Número de palavras na linha", "Número de linhas")


# Compara o total de letras em cada linha do texto.
def compare_num_letras_linhas(lista, dicio, trials):
    original_occ = num_letras_linha(lista)
    original_hist = get_histogram(original_occ, 100)

    histogramas_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_occ = num_letras_linha(current_mockup)
        mockup_hist = get_histogram(mockup_occ, 100)
        histogramas_controle.append(mockup_hist)

    make_bar_comp_plot(original_hist, histogramas_controle, 40, 75, "Total de palavras na linha", "Número de linhas")


# Compara o total de letras em cada linha do texto.
def compare_num_linhas(lista, dicio, trials):
    original_occ = num_linhas(lista)
    original_hist = get_histogram(original_occ, 100)

    histogramas_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_occ = num_linhas(current_mockup)
        mockup_hist = get_histogram(mockup_occ, 100)
        histogramas_controle.append(mockup_hist)

    make_bar_comp_plot(original_hist, histogramas_controle, 2, 9, "Número de linhas", "Número de mensagens")


# Compara o total de letras em cada linha do texto.
def compare_distrib_palavras(lista, dicio, trials, tipo):
    original_occ = freq_palavras(texto_original, tipo)
    original_hist = get_histogram(original_occ, 100)

    histogramas_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_occ = freq_palavras(current_mockup, tipo)
        mockup_hist = get_histogram(mockup_occ, 100)
        histogramas_controle.append(mockup_hist)

    make_bar_comp_plot(original_hist, histogramas_controle, 1, 20, "Número de palavras com repetições", "Número de repetições")


def compare_freq_letras(lista, dicio, trials, tipo):
    original_dic = freq_letras(texto_original, tipo)
    dics_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_dic = freq_letras(current_mockup, tipo)
        dics_controle.append(mockup_dic)

    means_dics = find_mean_dict(dics_controle, original_dic)
    max_dics = get_max_min_dict(dics_controle, original_dic, 1)
    min_dics = get_max_min_dict(dics_controle, original_dic, 2)
    make_label_bar_plot(original_dic, means_dics, max_dics, min_dics, "Letras", "Ocorrências")

# Faz os cálculos de n e m
def compare_n_m(lista, dicio, trials, n_maximo, m_maximo, titulos=False):
    mockups = []
    matriz = [[0] * (m_maximo+1) for _ in range(n_maximo+1)]

    for n_num in range(n_maximo+1):
        matriz[n_num][0] = n_num

    for m_num in range(m_maximo+1):
        matriz[0][m_num] = m_num
    matriz[0][0] = ' '

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockups.append(current_mockup)

    for n in range(n_maximo):
        for m in range(m_maximo):
            if titulos:
                original_dic = freq_nesimas_letras_linhas_titulos(texto_original, n, m)
            else:
                original_dic = freq_nesimas_letras_linhas_palavras(texto_original, n, m)

            dics_controle = []
            for mock in mockups:
                if titulos:
                    mockup_dic = freq_nesimas_letras_linhas_titulos(mock, n, m)
                else:
                    mockup_dic = freq_nesimas_letras_linhas_palavras(mock, n, m)

                #print(mockup_dic)
                dics_controle.append(mockup_dic)

            means_dics = find_mean_dict(dics_controle, original_dic)
            max_dics = get_max_min_dict(dics_controle, original_dic, 1)
            min_dics = get_max_min_dict(dics_controle, original_dic, 2)

            #print("Fazendo para " + str(n) + "-" + str(m))
            matriz[n+1][m+1] = count_outliers(original_dic, means_dics, max_dics, min_dics)

    return matriz

def analises_m_n(n, m, titulo):
    print("A matriz para o texto original é: ")
    single_mock = load_mockup(dicio_texto_titulo, dicio_texto_titulo, 618)
    original = compare_n_m(texto_original, dicio_texto_titulo, 100, n, m, titulo)
    print(tabulate(original))
    print("A matriz para um texto de controle qualquer é: ")
    controle = compare_n_m(single_mock, dicio_texto_titulo, 100, n, m,titulo)
    print(tabulate(controle))

# Faz a checagem dos dicionários.
def checar_dicios():
    # def check_dicio(lista, dicio1, dicio2=None, usar2=False, tipo=None):
    demo_provavel_t_t = check_dicio(texto_original, dicio_texto_titulo)
    demo_improvavel_t_t = check_dicio(texto_original, dicio_texto_titulo, None, False, [3])
    print("O primeiro dicionário possui 100% dos textos e títulos: ")
    print([item for item, count in collections.Counter(demo_provavel_t_t).items()])
    print("Mas não para autor: ")
    print([item for item, count in collections.Counter(demo_improvavel_t_t).items()])
    print("Porém, o outro dicionário possui 100% dos autores se usado em combinação com o primeiro: ")
    demo_errado = check_dicio(texto_original, dicio_texto_titulo, dicio_autor_errado, True, [3])
    print("Mas não sozinho:")
    demo_errado = check_dicio(texto_original, dicio_autor_errado, dicio_texto_titulo, False, [3])
    print([item for item, count in collections.Counter(demo_errado).items()])

def compare_enesimas_letras(lista, dicio,trials, n,m ):
    original_dic = freq_nesimas_letras_linhas_palavras(lista, n, m)
    dics_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_dic = freq_nesimas_letras_linhas_palavras(current_mockup, n, m)
        dics_controle.append(mockup_dic)

    means_dics = find_mean_dict(dics_controle, original_dic)
    max_dics = get_max_min_dict(dics_controle, original_dic, 1)
    min_dics = get_max_min_dict(dics_controle, original_dic, 2)

    make_label_bar_plot(original_dic, means_dics, max_dics, min_dics, "Letras", "Ocorrências")


def compare_enesimas_letras_titulos(lista, dicio,trials, n,m ):
    original_dic = freq_nesimas_letras_linhas_titulos(lista, n, m)
    dics_controle = []

    for i in range(trials):
        current_mockup = load_mockup(dicio, dicio_autor_errado, len(lista))
        mockup_dic = freq_nesimas_letras_linhas_titulos(current_mockup, n, m)
        dics_controle.append(mockup_dic)

    means_dics = find_mean_dict(dics_controle, original_dic)
    max_dics = get_max_min_dict(dics_controle, original_dic, 1)
    min_dics = get_max_min_dict(dics_controle, original_dic, 2)

    make_label_bar_plot(original_dic, means_dics, max_dics, min_dics, "Letras", "Ocorrências")



# 0) Operações obrigatórias

# a) Carregar todas as mensagens
texto_original = load_objects()

# b) Carregar os possíveis dicionários
dicio_texto_titulo = load_dicio('NewLista.txt')
dicio_autor_errado = load_dicio('NomesLista.txt')

# 1) Operações descritivas

# a) Como as linhas se distribuem?
#compare_num_linhas(texto_original, dicio_texto_titulo, 100)

# b) Como o total de letras por linha se comporta?
#compare_num_letras_linhas(texto_original,dicio_texto_titulo,100)

# c) Como o total de palavras nas linhas se comporta?
#compare_num_palavras_linhas(texto_original, dicio_texto_titulo, 100)

# d) Como o total de palavras nas mensagens de comporta?
#compare_num_palavras(texto_original, dicio_texto_titulo, 100,1)

# 2) Análises de repetição

# a) Quais letras são mais frequentes?
#compare_freq_letras(texto_original,dicio_texto_titulo, 100,1)

# b) Como que palavras se repetem?
#compare_distrib_palavras(texto_original,dicio_texto_titulo,100,1)

# c) E as n-ésimas letras e m-ésimas palavras?
n_valor = 14
m_valor = 14
#compare_enesimas_letras(texto_original, dicio_texto_titulo,100, n_valor,m_valor)

# 3) Análise numérica de frequência n e m
#analises_m_n(n_valor, m_valor, False)

# 4) Análise dos títulos

# a) Número de palavras
#compare_num_palavras(texto_original, dicio_texto_titulo, 100,2)

# b) Repetições de palavras
#compare_distrib_palavras(texto_original,dicio_texto_titulo,100,2)

# c) Repetições de letras
#compare_freq_letras(texto_original,dicio_texto_titulo, 100,2)

# d) Matriz n-m
n_valor = 14
m_valor = 3
#analises_m_n(n_valor, m_valor, True)

# 5) Análises dos autores

# a) Checagem de dicionário
#checar_dicios()

# b) Número de palavras
#compare_num_palavras(texto_original, dicio_texto_titulo, 100,3)

# c) Frequências de letras
compare_freq_letras(texto_original,dicio_texto_titulo, 100,3)

# d) Frequências repetições
compare_distrib_palavras(texto_original,dicio_texto_titulo,100,3)