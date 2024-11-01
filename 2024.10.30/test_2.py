def is_valid(word: str) -> bool:
    return word.isalpha()


def test():
    assert is_valid('kijhkjghkjg') == True
    assert is_valid("jhkgjfgt ") == False
    assert is_valid("jhkgjfgt1") == False
    assert is_valid("jhkgjfgt.") == False
    assert is_valid("") == False


def test_all_words():
    # достать все слова
    with open("words.txt", 'r', encoding="UTF-8") as file:
        # пройтись циклом по каждому
        for word in file:
            # проверить каждое с помощью assert
            assert is_valid(word.strip()) == True
