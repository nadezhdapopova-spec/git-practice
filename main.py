import os

from src.get_name_list import clear_names


def main() -> None:
    """Вывод списка имен, содержащихся в файле"""
    current_directory = os.getcwd()
    file_name = os.path.join(current_directory, r"data/names.txt")

    cleared_names = clear_names(file_name)

    for name in cleared_names:
        print(name)


main()
