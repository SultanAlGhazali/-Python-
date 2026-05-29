# =======================================================
# Лабораторна робота №4. Об'єктно-орієнтоване програмування
# Студент: Аль-Газалі Султан, Група: {З-31}В, Варіант: 1
# =======================================================

class Book:
    """Базовий клас, що описує книгу."""
    def __init__(self, title, author, year):
        self.title = title        # Назва книги
        self.author = author      # Автор
        self.year = year          # Рік видання

    def get_info(self):
        """Метод для виведення базової інформації про книгу."""
        return f"Книга: '{self.title}', Автор: {self.author}, Рік: {self.year}"


class EBook(Book):
    """Похідний клас (наслідування) для електронних книг."""
    def __init__(self, title, author, year, file_size, file_format):
        # Викликаємо конструктор базового класу
        super().__init__(title, author, year)
        self.file_size = file_size    # Розмір файлу в Мб
        self.file_format = file_format  # Формат (pdf, epub і т.д.)

    def get_info(self):
        """Перевизначення методу (поліморфізм) для електронної книги."""
        base_info = super().get_info()
        return f"{base_info} [Е-версія: {self.file_format}, Розмір: {self.file_size}MB]"


def main():
    print("--- Демонстрація роботи класів (ООП) ---\n")

    # Створюємо об'єкт базового класу (паперова книга)
    paper_book = Book("Кобзар", "Тарас Шевченко", 1840)
    print(paper_book.get_info())

    # Створюємо об'єкт похідного класу (електронна книга)
    digital_book = EBook("Python для початківців", "А. Елс", 2023, 4.5, "PDF")
    print(digital_book.get_info())


if __name__ == "__main__":
    main()
