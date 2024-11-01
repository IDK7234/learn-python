import os
from pathlib import Path
from zipfile import ZipFile
from second_layer import getting_words

def parsing(name):
    words: list = []
    words_not_split = ""

    with ZipFile(name) as archive:
        for f in archive.namelist():
            words_not_split += (getting_words(archive.open(f)))

    words = words_not_split.split('\n')
    words.pop()

    for i in range(len(words)):
        print(f"[{i + 1}] {words[i]}")