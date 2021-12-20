# Classe para o objeto mensagem.
class Message(object):
    # Constructor.
    def __init__(self, file, author, title, text):
        self.file = file
        self.author = author
        self.title = title
        self.text = text

    def print(self):
        print("Arquivo: " + self.file)
        print("Autor: " + self.author)
        print("Título: " + self.title)
        print("Texto: " + self.text)
        print("------------------------------------------------------------------------------------------")