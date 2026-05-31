import os
import glob


# =====================================================================
# 1. ФУНКЦІЇ ДЛЯ СТВОРЕННЯ ТА ЗАПИСУ ДАНИХ
# =====================================================================
def create_group_file(filename, students_data):
    """Створює файл групи та записує початкові дані (Ім'я та Середній бал)"""
    # Режим 'w' очищує файл, якщо він існував, або створює новий
    with open(filename, "w", encoding="utf-8") as f:
        for student, grade in students_data:
            f.write(f"{student}\t{grade}\n")
    print(f"Файл '{filename}' успішно створено та заповнено.")


def append_student(filename, student_name, grade):
    """Дозаписує одного нового студента в кінець існуючого файлу"""
    # Режим 'a' (append) додає дані в кінець файлу, не видаляючи старі
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{student_name}\t{grade}\n")
    print(f"Студента {student_name} успішно додано до файлу {filename}.")


# =====================================================================
# 2. ФУНКЦІЇ ДЛЯ ПОШУКУ ТА ЧИТАННЯ
# =====================================================================
def find_group_files():
    """Шукає всі файли груп у поточній директорії за маскою '*.txt'"""
    print("\nПошук файлів груп у каталозі:")
    # Використовуємо бібліотеку glob для пошуку за маскою
    files = glob.glob("група_*.txt")
    for file in files:
        print(f" - Знайдено файл групи: {file}")
    return files


def search_student_in_file(filename, search_name):
    """Шукає студента у конкретному файлі за його ім'ям"""
    print(f"\nПошук студента '{search_name}' у файлі {filename}:")
    found = False

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # Очищаємо рядок від знаків переносу \n та ділимо по табуляції
            data = line.strip().split("\t")
            if data and data[0].lower() == search_name.lower():
                print(f"-> Знайдено! Студент: {data[0]}, Середній бал: {data[1]}")
                found = True
                break

    if not found:
        print("-> Такого студента в цій групі не знайдено.")


# =====================================================================
# 3. ФУНКЦІЯ СОРТУВАННЯ ЗА СЕРЕДНІМ БАЛОМ
# =====================================================================
def sort_students_by_grade(filename):
    """Зчитує дані, сортує студентів за спаданням балу та виводить результат"""
    print(f"\nСортування студентів файлу {filename} за середнім балом (від вищого до нижчого):")
    students = []

    # Читання даних
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("\t")
            if len(data) == 2:
                name = data[0]
                grade = float(data[1])  # Конвертуємо бал у число для коректного сортування
                students.append((name, grade))

    # Сортування списку кортежів за другим елементом (grade) у зворотньому порядку (reverse=True)
    students.sort(key=lambda item: item[1], reverse=True)

    # Виведення відсортованих даних
    for rank, (name, grade) in enumerate(students, 1):
        print(f"{rank}. {name} — {grade}")


# =====================================================================
# ОСНОВНА ПРОГРАМА (ДЕМОНСТРАЦІЯ РОБОТИ)
# =====================================================================
if __name__ == "__main__":
    # Початкові дані для двох груп
    group_1_data = [
        ("Іванов Іван", 4.5),
        ("Петров Петро", 3.8),
        ("Сидоров Олег", 4.9)
    ]

    group_2_data = [
        ("Коваленко Анна", 4.2),
        ("Мельник Дмитро", 4.7),
        ("Шевченко Ольга", 3.5)
    ]

    # Ім'я файлів
    file_g1 = "група_1.txt"
    file_g2 = "група_2.txt"

    print("--- Крок 1: Запис та створення файлів ---")
    create_group_file(file_g1, group_1_data)
    create_group_file(file_g2, group_2_data)

    print("\n--- Крок 2: Дозапис даних у файл ---")
    # Додамо по одному студенту в кожну групу
    append_student(file_g1, "Васильєва Олена", 4.6)
    append_student(file_g2, "Ткаченко Сергій", 5.0)

    print("\n--- Крок 3: Пошук файлів у каталозі за маскою ---")
    find_group_files()

    print("\n--- Крок 4: Пошук даних усередині файлу ---")
    search_student_in_file(file_g1, "Петров Петро")
    search_student_in_file(file_g1, "Неіснуючий Студент")

    print("\n--- Крок 5: Сортування даних за середнім балом ---")
    sort_students_by_grade(file_g1)
    sort_students_by_grade(file_g2)
