# =======================================================
# Лабораторна робота №3. Робота з рядками та файлами
# Студент: Аль-Газалі Султан, Група: {З-31}В, Варіант: 1
# =======================================================

import os


def process_text(text):
    """
    Завдання: Знайти найдовше слово у тексті та порахувати
    кількість розділових знаків (крапок, ком і т.д.).
    """
    # 1. Пошук найдовшого слова
    # Очищаємо текст від основних розділових знаків для коректного пошуку слів
    cleaned_text = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ')
    words = cleaned_text.split()

    if words:
        longest_word = max(words, key=len)
    else:
        longest_word = "Слів не знайдено"

    # 2. Підрахунок розділових знаків
    punctuation_marks = ".,;:!?-"
    punc_count = sum(1 for char in text if char in punctuation_marks)

    return longest_word, punc_count


def main():
    filename = "input_text.txt"

    # Створюємо тестовий файл, якщо його немає, щоб програма не падала
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Привіт, Султан! Це тестовий текст для лабораторної роботи номер три. Бажаю успіху!")

    print(f"Зчитуємо дані з файлу: {filename}\n")

    # Безпечне читання з файлу за допомогою try-except
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        print(f"Вміст файлу:\n\"{content}\"\n")

        # Обробка тексту
        longest, punc_sum = process_text(content)

        # Виведення результатів
        print(f"Результати аналізу:")
        print(f"- Найдовше слово у тексті: {longest} (довжина: {len(longest)} симв.)")
        print(f"- Кількість розділових знаків: {punc_sum}")

    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено!")
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")


if __name__ == "__main__":
    main()
