
def Sep(line: str, sep: str):
    return line.split(sep)

if __name__ == '__main__':
    a1 = str(input("Enter your line: "))
    a2 = str(input("Enter separator: "))
    print(Sep(a1, a2))