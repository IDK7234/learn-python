def sep(line: str, sep):
    result: list[str] = ['']
    c = True
    for i in line:
        if c:
            if i in sep:
                c = False

        else:
            if i not in sep and i != " ":
                result.append('')
                c = True

        result[-1] += i

    return result

if __name__ == '__main__':
    separators: list[str] = [';', '.', '!', '?']
    test_string = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.."
    print(sep(test_string, separators))
