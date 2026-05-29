# =======================================================
# Лабораторна робота №2. Модуль з функціями
# Студент: Аль-Газалі Султан, Група: {З-31}В, Варіант: 1
# =======================================================

def bubble_sort(lst):
    """1. Бульбашкове сортування."""
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def find_element(lst, value):
    """2. Пошук елементу за значенням."""
    try:
        return lst.index(value)
    except ValueError:
        return -1

def find_sequence(lst, seq):
    """3. Пошук послідовності елементів."""
    n, m = len(lst), len(seq)
    for i in range(n - m + 1):
        if lst[i:i + m] == seq:
            return i
    return -1

def find_five_min(lst):
    """4. Пошук перших п’яти мінімальних елементів."""
    return sorted(lst)[:5]

def find_five_max(lst):
    """5. Пошук перших п’яти максимальних елементів."""
    return sorted(lst, reverse=True)[:5]

def find_average(lst):
    """6. Пошук середнього арифметичного."""
    return sum(lst) / len(lst) if lst else 0

def remove_duplicates(lst):
    """7. Повернення списку без повторів."""
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
