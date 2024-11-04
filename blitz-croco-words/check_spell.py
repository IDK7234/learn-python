import pyaspeller

def check(a:list):
    b:list = []
    for i in range(len(a)):
        b.append(pyaspeller.YandexSpeller().spelled(a[i]))
    return b

if __name__ == '__main__':
    a: list = ["Колакал", "Малако"]
    print(check(a))