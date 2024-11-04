import pyaspeller

def check(a:list):

    return pyaspeller.YandexSpeller().spelled(' '.join(a))


if __name__ == '__main__':
    a: list = ["Колакал", "Малако"]
    print(check(a))