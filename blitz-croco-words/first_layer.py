import os
from pathlib import Path
from zipfile import ZipFile
from second_layer import getting_words

def without_duplicates(a:list):
    words_without_duplicates = []
    for i in range(len(a)):
        if a[i] not in words_without_duplicates:
            words_without_duplicates.append(a[i])
    return words_without_duplicates


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

    print("____________________________________________")

    words_n_d = without_duplicates(words)

    for i in range(len(words_n_d)):
        print(f"[{i + 1}] without_duplicates {words_n_d[i]}")