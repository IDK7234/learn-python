def sep(line: str, sep: str) -> list():
    return line.split(sep)


if __name__ == '__main__':
    a2 = str(input("Enter separator: "))
    print(sep("I wanna:live/forever,something", a2))
