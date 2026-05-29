# =======================================================
# Лабораторна робота №2. Головний файл програми
# Студент: Аль-Газалі Султан, Група: {З-31}В, Варіант: 1
# =======================================================
import mymodule

# Створюємо тестовий список для демонстрації роботи модуля
test_list = [5, 3, 8, 5, 2, 8, 1, 9, 4, 7, 6, 2]
print(f"Початковий список: {test_list}")

# 1. Сортування
sorted_list = mymodule.bubble_sort(test_list.copy())
print(f"1. Відсортований список: {sorted_list}")

# 2. Пошук елемента
idx = mymodule.find_element(test_list, 8)
print(f"2. Індекс елемента '8': {idx}")

# 3. Пошук послідовності
seq_idx = mymodule.find_sequence(test_list, [8, 5])
print(f"3. Індекс послідовності [8, 5]: {seq_idx}")

# 4. П'ять мінімальних
print(f"4. Перші 5 мінімальних: {mymodule.find_five_min(test_list)}")

# 5. П'ять максимальних
print(f"5. Перші 5 maximal: {mymodule.find_five_max(test_list)}")

# 6. Середнє арифметичне
print(f"6. Середнє арифметичне: {mymodule.find_average(test_list):.2f}")

# 7. Видалення повторів
print(f"7. Список без повторів: {mymodule.remove_duplicates(test_list)}")
