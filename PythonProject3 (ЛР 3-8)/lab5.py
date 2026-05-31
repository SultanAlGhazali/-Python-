"""
Лабораторна робота №5 (Варіант 1)
Тема: Об’єктно-орієнтоване програмування у мові Python
Мета: Навчитися створювати класи, об'єкти, методи та використовувати принципи ООП.
"""


class Student:
    """Клас, що описує модель студента університету"""

    def __init__(self, name: str, age: int, average_grade: float):
        """Конструктор класу — ініціалізує атрибути об'єкта студента"""
        self.name = name  # Ім'я та прізвище
        self.age = age  # Вік
        self.average_grade = average_grade  # Середній бал

    def __str__(self):
        """Магічний метод для красивого виведення інформації про студента у print()"""
        return f"Студент: {self.name:<20} | Вік: {self.age} | Середній бал: {self.average_grade:.2f}"


class GroupManager:
    """Клас для керування списком студентів (масивом об'єктів)"""

    def __init__(self, group_name: str):
        """Ініціалізація групи порожнім списком студентів"""
        self.group_name = group_name
        self.students_list = []  # Масив (список) для збереження об'єктів класу Student

    def add_student(self, student: Student):
        """Метод додавання нового об'єкта студента до групи"""
        self.students_list.append(student)
        print(f"👍 Студента '{student.name}' успішно додано до групи {self.group_name}.")

    def show_all_students(self):
        """Метод для виведення всього списку студентів групи"""
        print(f"\n--- Список студентів групи {self.group_name} ---")
        if not self.students_list:
            print("Група порожня.")
            return
        for student in self.students_list:
            print(student)  # Автоматично викликає метод __str__ класу Student

    def get_average_group_grade(self) -> float:
        """Метод обчислення середнього балу всієї групи"""
        if not self.students_list:
            return 0.0
        total_sum = sum(student.average_grade for student in self.students_list)
        return total_sum / len(self.students_list)

    def find_top_students(self, threshold=4.5):
        """Метод пошуку відмінників, у яких бал вищий за заданий поріг"""
        print(f"\n--- Студенти групи {self.group_name} із балом вище {threshold} ---")
        found = False
        for student in self.students_list:
            if student.average_grade >= threshold:
                print(student)
                found = True
        if not found:
            print("Таких студентів немає.")


# =====================================================================
# ДЕМОНСТРАЦІЯ РОБОТИ КЛАСІВ (ОСНОВНА ПРОГРАМА)
# =====================================================================
if __name__ == "__main__":
    print("=== ЛАБОРАТОРНА РОБОТА №5: ОБ'ЄКТНО-ОРІЄНТОВАНЕ ПРОГРАМУВАННЯ ===")

    # 1. Створення менеджера групи (об'єкт класу GroupManager)
    my_group = GroupManager(group_name='{З-31}В')
    print()

    # 2. Створення окремих об'єктів студентів (екземпляри класу Student)
    student1 = Student(name="Іванов Іван", age=20, average_grade=4.2)
    student2 = Student(name="Сидоров Олег", age=19, average_grade=4.9)
    student3 = Student(name="Васильєва Олена", age=21, average_grade=4.7)
    student4 = Student(name="Петров Петро", age=20, average_grade=3.8)

    # 3. Додавання студентів до групи за допомогою методу об'єкта групи
    my_group.add_student(student1)
    my_group.add_student(student2)
    my_group.add_student(student3)
    my_group.add_student(student4)

    # 4. Виведення всього списку за допомогою методу класу
    my_group.show_all_students()

    # 5. Розрахунок середньої успішності по групі
    group_avg = my_group.get_average_group_grade()
    print(f"\n📊 Середній бал групи {my_group.group_name}: {group_avg:.2f}")

    # 6. Фільтрація та пошук кращих студентів групи
    my_group.find_top_students(threshold=4.5)
