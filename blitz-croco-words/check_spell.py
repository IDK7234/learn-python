import pyaspeller

def check(a:list) -> list:
    return pyaspeller.YandexSpeller().spelled(' '.join(a)).split(" ")

