"""
Модуль для лабораторної роботи №4 (Варіант 1).
Містить інструменти для базової та кастомної роботи з рядками.
"""

def string_info(s):
    """
    Повертає довжину рядка, перший та останній символи.
    :param s: Вхідний рядок (str)
    :return: Кортеж (довжина, перший_символ, останній_символ)
    """
    if not s:
        return 0, "", ""
    return len(s), s[0], s[-1]

def string_reverse(s):
    """
    Розгортає рядок у зворотному напрямку за допомогою зрізів.
    :param s: Вхідний рядок (str)
    :return: Перевернутий рядок (str)
    """
    return s[::-1]

def clear_whitespace(s):
    """
    Видаляє всі пробіли на початку та в кінці рядка.
    :param s: Вхідний рядок (str)
    :return: Очищений рядок (str)
    """
    return s.strip()

def count_substring(s, sub):
    """
    Рахує кількість входжень підрядка в рядок без перетинів.
    :param s: Головний рядок (str)
    :param sub: Підрядок для пошуку (str)
    :return: Кількість входжень (int)
    """
    return s.count(sub)

def replace_substring(s, old, new):
    """
    Замінює всі входження одного підрядка на інший.
    :param s: Вхідний рядок (str)
    :param old: Що замінити (str)
    :param new: На що замінити (str)
    :return: Новий рядок із замінами (str)
    """
    return s.replace(old, new)

def check_string_type(s):
    """
    Перевіряє, з яких символів складається рядок.
    :param s: Вхідний рядок (str)
    :return: Рядок-опис типу вмісту (str)
    """
    if s.isdigit():
        return "Рядок складається тільки з цифр"
    elif s.isalpha():
        return "Рядок складається тільки з літер"
    elif s.isalnum():
        return "Рядок містить як літери, так і цифри"
    elif s.isspace():
        return "Рядок складається тільки з невідображуваних символів (пробілів)"
    else:
        return "Рядок містить змішані символи або спецсимволи"

def merge_list_to_string(lst, separator=" "):
    """
    Збирає список рядків в один рядок із заданим роздільником.
    :param lst: Список елементів (list)
    :param separator: Роздільник між елементами (str)
    :return: Сформований рядок (str)
    """
    return separator.join([str(elem) for elem in lst])
