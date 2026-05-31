import string_utils

if __name__ == "__main__":
    print("=== ЛАБОРАТОРНА РОБОТА №4: РОБОТА З РЯДКАМИ ===")

    # 1. Демонстрація Doc strings (за вимогою методички)
    print("\n--- Перевірка наявності Doc String для однієї з функцій ---")
    print(string_utils.check_string_type.__doc__)

    # Тестовий рядок для роботи
    test_str = "   Кафедра кібербезпеки та програмного забезпечення 2026   "
    print(f"\nПочатковий тестовий рядок:\n'{test_str}'")

    # 2. Виклик функції 1: Інформація про рядок
    length, first, last = string_utils.string_info(test_str)
    print(f"\n1. Довжина початкового рядка: {length}. Перший символ: '{first}', Останній: '{last}'")

    # 3. Виклик функції 2: Реверс рядка
    reversed_str = string_utils.string_reverse(test_str.strip())
    print(f"2. Рядок у зворотному порядку (без крайових пробілів): '{reversed_str}'")

    # 4. Виклик функції 3: Очищення від пробілів
    clean_str = string_utils.clear_whitespace(test_str)
    print(f"3. Рядок після очищення крайових пробілів (.strip()): '{clean_str}'")

    # 5. Виклик функції 4: Пошук кількості входжень підрядка
    sub = "а"
    count = string_utils.count_substring(clean_str, sub)
    print(f"4. Літера '{sub}' зустрічається у рядку {count} раз(и)")

    # 6. Виклик функції 5: Заміна підрядка
    replaced = string_utils.replace_substring(clean_str, "2026", "ЦНТУ")
    print(f"5. Рядок після заміни року на абревіатуру: '{replaced}'")

    # 7. Виклик функції 6: Перевірка типу рядка за допомогою вбудованих методів
    print("\n6. Тестування аналізу вмісту рядків:")
    print(f"   - '{clean_str}': {string_utils.check_string_type(clean_str)}")
    print(f"   - '45210': {string_utils.check_string_type('45210')}")
    print(f"   - 'Python': {string_utils.check_string_type('Python')}")

    # 8. Виклик функції 7: Збірка рядка зі списку
    words_list = ["Скриптові", "мови", "програмування", "Python"]
    joined_str = string_utils.merge_list_to_string(words_list, separator=" -> ")
    print(f"\n7. Збірка рядка зі списку елементів:\n   {joined_str}")
