def sep(line: str, sep):
    a: str = ""
    x = line.replace(" ", "")
    for i in x:
        a += i
        if i in sep:
            if a != x:
                a += " "

    z = a.split(" ")
    z.pop(-1)
    return z

if __name__ == '__main__':
    a2 = [';', '.']
    print(sep("Строка1; Строка2. Строка3.", a2))
