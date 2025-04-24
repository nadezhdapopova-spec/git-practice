def clear_names(file_name: str) -> list:
    """Функция для очистки имен от лишних символов"""
    name_list = []
    with open(file_name, "r", encoding="utf-8") as names_file:
        lines = names_file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            name = ""
            for ch in line:
                if ch.isalpha():
                    name += ch
            if name != "":
                name_list.append(name)
    return name_list


def filter_latin_names(file_name: str) -> list:
    """Получение списка имен из файла на латиннице"""
    latin_names = []
    latin_alphabet = [chr(i) for i in range(97, 123)]

    with open(file_name, "r", encoding="utf-8") as names_file:
        lines = names_file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            name = ""
            for ch in line:
                if ch.lower() in latin_alphabet:
                    name += ch
            if name != "":
                latin_names.append(name)

    return latin_names


def filter_cyrillic_names(file_name: str) -> list:
    """Получение списка имен из файла на кириллице"""
    cyrillic_names = []
    a = ord("а")
    rus_alphabet = [chr(i) for i in range(a, a + 32)]

    with open(file_name, "r", encoding="utf-8") as names_file:
        lines = names_file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            name = ""
            for ch in line:
                if ch.lower() in rus_alphabet:
                    name += ch
            if name != "":
                cyrillic_names.append(name)

    return cyrillic_names
