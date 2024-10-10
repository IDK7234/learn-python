def split_text_by_separators(text: str, seps: list[str]) -> list[str]:  #Создаем функцию
    result: list[str] = ['']  #Создаем список result с 1 элементом
    waiting_for_separator: bool = True  #Создаем флажок

    for symbol in text:  #Запускаем функцию которая идет по элементам в строке
        if waiting_for_separator:  #Если флажок равен True
            if symbol in seps:  #Если символ в списке сепараторов
                waiting_for_separator = False  #Ставим флажок на False
        else:  #Или
            if not symbol in seps and symbol != ' ':  #Если символ не сепаратор и не пробел
                result.append('')  #Создаем новый элемент в result
                waiting_for_separator = True  #Ставим значение на True

        result[-1] += symbol  #Добавляем в конец элемента наш символ

    return result  #Возвращаем result


if __name__ == "__main__":  #Main
    separators: list[str] = [';', '.', '!', '?']  #Создаем список сепараторов
    test_string = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.."  #Создаем строку
    print(split_text_by_separators(test_string, separators))  #Печатаем то что возвращает наша функция с нашими параметрами
