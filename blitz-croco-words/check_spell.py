import pyaspeller

def check(a:list):
    text = ""
    for i in range(len(a)):
        text += a[i] + " "
    text_new = pyaspeller.YandexSpeller().spelled(text)
    text_new.split(" ")
    return text_new

if __name__ == '__main__':
    a: list = ["Колакал", "Малако"]
    print(check(a))