import pytest
from StringUtils import StringUtils

utils = StringUtils()
param = pytest.mark.parametrize
xfail = pytest.mark.xfail

# Capitilize
# Позитивные тесты


@param("text, result", [
    ("world", "World"),
    ("Text", "Text"),
    ("TEST", "TEST"),
    ("hELLO", "HELLO"),
    ("домашняя работа", "Домашняя работа"),
    ("номер 1", "Номер 1"),
    ("почта содержит @", "Почта содержит @"),
    ("1 сентября", "1 сентября")
    ])
def test_capitilize_positive(text, result):
    assert utils.capitilize(text) == result

# Негативные тесты


@xfail(strict=True)
def test_capitilize_negative_empty():
    assert utils.capitilize("") == ""


@xfail(strict=True)
def test_capitilize_negative_nums():
    assert utils.capitilize(2024) == 2024


@xfail(strict=True)
def test_capitilize_negative_boolean():
    assert utils.capitilize(True) == True


@xfail(strict=True)
def test_capitilize_negative_space():
    assert utils.capitilize(" ") == " "


@xfail(strict=True)
def test_capitilize_negative_none():
    assert utils.capitilize(None) == None


# Trim
# Позитивные тесты


@param("text, result", [
    (" world", "world"),
    ("  Привет", "Привет"),
    ("Book", "Book"),
    (" 0 градусов", "0 градусов"),
    (" Птица ", "Птица "),
    (" White Book", "White Book")
    ])
def test_trim_positive(text, result):
    assert utils.trim(text) == result

# Негативные тесты


@xfail(strict=True)
def test_trim_negative_space():
    assert utils.trim(" ") == " "


@xfail(strict=True)
def test_trim_negative_nums():
    assert utils.trim(2000) == 2000


@xfail(strict=True)
def test_trim_negative_empty():
    assert utils.trim("") == ""


@xfail(strict=True)
def test_trim_negative_boolean():
    assert utils.trim(False) == False


@xfail(strict=True)
def test_trim_negative_none():
    assert utils.trim(None) == None

# To list
# Позитивные тесты


@param("string, delimeter, list", [
    (("кукла,машинка,мишка,робот"), ",", ["кукла", "машинка", "мишка", "робот"]),
    (("1*2*3*4*5"), "*", ["1", "2", "3", "4", "5"]),
    (("Samsung,iPhone,Nokia", None, ["Samsung", "iPhone", "Nokia"])),
    (("1@2@3@4@5"), None, ["1@2@3@4@5"]),
    (("литература/ "), "/", ["литература", " "]),
    (("english"), None, ["english"])
    ])
def test_to_list_positive(string, delimeter, list):
    if delimeter is None:
        assert utils.to_list(string) == list
    else:
        assert utils.to_list(string, delimeter) == list

# Негативные тесты


@xfail(strict=True)
def test_to_list_negative_empty():
    assert utils.to_list("", None) == []


@xfail(strict=True)
def test_to_list_negative_none():
    assert utils.to_list(None, None) == None


@xfail(strict=True)
def test_to_list_negative_space():
    assert utils.to_list(" ", None) == []


@xfail(strict=True)
def test_to_list_negative_num():
    assert utils.to_list(1/2/3, "/") == ["1", "2", "3"]


# Contains


@param("string, symbol, result", [
    # позитивные тесты
    ("лошадь", "л", True),
    ("rain", "n", True),
    ("dima@mail.ru", "@", True),
    ("сонце", "л", False),
    ("1235", "4", False),
    # негативные
    pytest.param("лесница", "т", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(" ", " ", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param("", "", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(1234, 4, True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(None, None, None, marks=pytest.mark.xfail(strict=True)),
    pytest.param(False, None, False, marks=pytest.mark.xfail(strict=True)),
    pytest.param("12345", None, False, marks=pytest.mark.xfail(strict=True))
])
def test_contains(string, symbol, result):
    assert utils.contains(string, symbol) == result


# Delete symbol


@param("string, symbol, result", [
    # позитивные тесты
    ("слон", "л", "сон"),
    ("кинотеатр", "театр", "кино"),
    ("number 1234", "123", "number 4"),
    ("cate", "e", "cat"),
    ("Волан-де-Морт", "-", "ВоландеМорт"),
    ("Helllo", "l", "Heo"),
    ("пол день", " ", "полдень"),
    ("1", "1", ""),
    ("картофель", "ш", "картофель"),
    ("123, 124, 125, 126", " 124,", "123, 125, 126"),

    # негативные тесты
    pytest.param("", "", "", marks=pytest.mark.xfail(strict=True)),
    pytest.param(" ", " ", " ", marks=pytest.mark.xfail(strict=True)),
    pytest.param(None, None, None, marks=pytest.mark.xfail(strict=True)),
    pytest.param(True, None, True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(12345, 3, 1245, marks=pytest.mark.xfail(strict=True)),
])
def test_delete_symbol(string, symbol, result):
    assert utils.delete_symbol(string, symbol) == result


# Starts with


@param("string, symbol, result", [
    # позитивные тесты
    ("путеводитель", "п", True),
    ("Строка", "п", False),
    ("Mary", "M", True),
    ("собака", "соб", True),
    ("8911****", "8", True),
    ("@mail", "@", True),
    ("я", "я", True),
    # негативные тесты
    pytest.param("москва", "М", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param("Питер", "р", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param("дерево", "д", False, marks=pytest.mark.xfail(strict=True)),
    pytest.param("сад", None, False, marks=pytest.mark.xfail(strict=True)),
    pytest.param("", "", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(" ", " ", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(None, None, None, marks=pytest.mark.xfail(strict=True)),
    pytest.param(True, None, True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(12345, 1, True, marks=pytest.mark.xfail(strict=True)),
])
def test_starts_with(string, symbol, result):
    assert utils.starts_with(string, symbol) == result


# End with


@param("string, symbol, result", [
    # позитивные тесты
    ("путеводитель", "ь", True),
    ("строка", "о", False),
    ("телефоН", "Н", True),
    ("я", "я", True),
    ("dog", "og", True),
    ("8911", "11", True),
    ("Привет!", "!", True),
    # негативные тесты
    pytest.param("москва", "А", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param("питер", "п", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param("дерево", "о", False, marks=pytest.mark.xfail(strict=True)),
    pytest.param("сад", None, False, marks=pytest.mark.xfail(strict=True)),
    pytest.param("", "", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(" ", " ", True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(None, None, None, marks=pytest.mark.xfail(strict=True)),
    pytest.param(True, None, True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(12345, 5, True, marks=pytest.mark.xfail(strict=True)),
])
def test_end_with(string, symbol, result):
    assert utils.end_with(string, symbol) == result


# Is empty


@param("string, result", [
    # позитивные тесты
    ("", True),
    (" ", True),
    ("кот", False),
    ("11", False),
    ("I", False),
    ("!@", False),
    # негативные
    pytest.param(11, False, marks=pytest.mark.xfail(strict=True)),
    pytest.param(None, True, marks=pytest.mark.xfail(strict=True)),
    pytest.param(False, False, marks=pytest.mark.xfail(strict=True)),
])
def test_is_empty(string, result):
    assert utils.is_empty(string) == result


# List to string


@param("lst, joiner, result", [
    # позитиивные тесты
    (["роза","фиалка","ромашка","тюльпан"], ",", "роза,фиалка,ромашка,тюльпан"),
    (["1", "2", "3"], None, ("1, 2, 3")),
    (["Masha", "Sasha", "Pasha"], "/", ("Masha/Sasha/Pasha")),
    ([1,2], "-", ("1-2")),
    (["Русский язык", "Английский язык", "Немецкий язык"], ". ", ("Русский язык. Английский язык. Немецкий язык")),
    # негативные тесты
    pytest.param([], None, (), marks=pytest.mark.xfail(strict=True)),
    pytest.param([None], None, (None), marks=pytest.mark.xfail(strict=True)),
    pytest.param([""], None, (), marks=pytest.mark.xfail(strict=True)),
    pytest.param([" "], None, (" "), marks=pytest.mark.xfail),
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        assert utils.list_to_string(lst) == result
    else:
        assert utils.list_to_string(lst, joiner) == result
