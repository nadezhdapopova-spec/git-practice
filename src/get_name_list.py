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
