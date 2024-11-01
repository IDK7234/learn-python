import random, zipfile
LIST = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

def CreateIt():
    string: str = ""
    for _ in range(10000):
        for _ in range(100):
            string += random.choice(LIST)
        string += '\n'

    with open("text.txt", 'w', encoding='UTF-8') as file:
        file.write(string)




if __name__ == '__main__':
    CreateIt()
    with zipfile.ZipFile('text.zip', 'w') as zipwr:
        zipwr.write("text.txt")




