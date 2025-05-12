from config import ROOT_DIR
import os
from src.get_name_list import clear_names, filter_cyrillic_names, filter_latin_names


def main_1() -> None:
    """Вывод списка имен, содержащихся в файле"""
    file_name = os.path.join(ROOT_DIR, r"data/names.txt")

    cleared_names = clear_names(file_name)

    for name in cleared_names:
        print(name)


main_1()


def main_2() -> None:
    """Создание файла с именами на английском языке"""
    file_name = os.path.join(ROOT_DIR, r"data/names.txt")

    latin_names = filter_latin_names(file_name)

    with open(r"data/eng_names.txt", "w", encoding="utf-8") as latin_names_file:
        latin_names_file.write("\n".join(latin_names))


main_2()


def main_3() -> None:
    """Создание файла с именами на русском языке"""
    current_directory = os.getcwd()
    file_name = os.path.join(current_directory, r"data/names.txt")

    cyrillic_names = filter_cyrillic_names(file_name)

    with open(r"data/rus_names.txt", "w", encoding="utf-8") as cyrillic_names_file:
        cyrillic_names_file.write("\n".join(cyrillic_names))


main_3()
