import pyaspeller

def check(a:str):
    return pyaspeller.YandexSpeller().spelled(a)

if __name__ == '__main__':
    print(check("Колакал малако"))