
def is_valid(word: str) -> bool:
    return word.isalpha()


def test():
    assert is_valid('kijhkjghkjg') == True
    assert is_valid("jhkgjfgt ") == False
    assert is_valid("jhkgjfgt1") == False
    assert is_valid("jhkgjfgt.") == False
    assert is_valid("") == False


