import os
import csv
import json

directory = 'paginas'

titles = []
authors = []
texts = []
filenames = []

def concat():
    with open('aaa.txt', 'w') as outfile:
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), encoding='utf8') as infile:
                for line in infile:
                    try:
                        outfile.write(line)
                    except:
                        print("Aaa")

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename), encoding='utf8') as infile:

        data = str(infile.readlines())

        filenames.append(filename)

        # Carrega o título

        current_title = data.partition('data-subject="')[2]
        current_title = current_title.partition('"')[0]
        titles.append(current_title)

        # Carrega o autor

        current_author = data.partition('data-author="')[2]
        current_author = current_author.partition('"')[0]
        authors.append(current_author)

        # Carrega o texto

        current_text = data.partition('role="region"><br>')[2]
        current_text = current_text.partition('<p>')[0]
        texts.append(current_text)


with open("filenames.json", 'w') as f:
    # indent=2 is not needed but makes the file human-readable
    json.dump(filenames, f, indent=2)

with open("authors.json", 'w') as a:
        # indent=2 is not needed but makes the file human-readable
        json.dump(authors, a, indent=2)

with open("titles.json", 'w') as tl:
    # indent=2 is not needed but makes the file human-readable
    json.dump(titles, tl, indent=2)

with open("texts.json", 'w') as te:
    # indent=2 is not needed but makes the file human-readable
    json.dump(texts, te, indent=2)