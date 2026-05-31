"""
Лабораторна робота №8 (Варіант 1)
Тема: Створення графічного інтерфейсу користувача за допомогою мови Python
Мета: Навчитися розробляти візуальні віконні застосунки за допомогою бібліотеки Tkinter.
"""

import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    """Функція-обробник для розрахунку ІМТ при натисканні на кнопку"""
    try:
        # Зчитуємо дані з текстових полів введення
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        # Перевіряємо на коректність (ріст має бути в метрах, наприклад 1.75)
        if height > 3.0:
            # Якщо користувач ввів ріст у сантиметрах (наприклад, 175), автоматично переводимо в метри
            height = height / 100.0

        # Формула ІМТ: вага (кг) / ріст^2 (м)
        bmi = weight / (height ** 2)

        # Визначаємо категорію та колір фону для результату
        if bmi < 18.5:
            category = "Недостатня вага (дефіцит)"
            color = "#3498db"  # Синій
        elif 18.5 <= bmi < 25.0:
            category = "Нормальна вага"
            color = "#2ecc71"  # Зелений
        elif 25.0 <= bmi < 30.0:
            category = "Надлишкова вага (предожиріння)"
            color = "#f1c40f"  # Жовтий
        else:
            category = "Ожиріння"
            color = "#e74c3c"  # Червоний

        # Оновлюємо текстові мітки в інтерфейсі для виведення результату
        label_result_value.config(text=f"{bmi:.2f}", fg=color)
        label_category_value.config(text=category, fg=color)

    except ValueError:
        # Обробка помилки, якщо користувач ввів літери замість чисел або залишив поля порожніми
        messagebox.onerror("Помилка введення", "Будь ласка, введіть коректні числові значення для ваги та росту!")


# =====================================================================
# СТВОРЕННЯ ГРАФІЧНОГО ІНТЕРФЕЙСУ (GUI)
# =====================================================================

# 1. Ініціалізація головного вікна програми
root = tk.Tk()
root.title("Калькулятор ІМТ — ЛР №8")
root.geometry("380x320")  # Встановлюємо розмір вікна
root.resizable(False, False)  # Забороняємо змінювати розміри вікна користувачем
root.configure(bg="#f5f6fa")  # Колір фону вікна

# Головний заголовок всередині вікна
label_title = tk.Label(root, text="Розрахунок індексу маси тіла", font=("Arial", 14, "bold"), bg="#f5f6fa",
                       fg="#2f3640")
label_title.pack(pady=15)

# 2. Блок введення ВАГИ
frame_weight = tk.Frame(root, bg="#f5f6fa")
frame_weight.pack(pady=5)

label_weight = tk.Label(frame_weight, text="Вага (кг):", font=("Arial", 11), bg="#f5f6fa", width=12, anchor="w")
label_weight.pack(side=tk.LEFT)

entry_weight = tk.Entry(frame_weight, font=("Arial", 11), width=10, bd=2, relief="groove")
entry_weight.pack(side=tk.LEFT)
entry_weight.insert(0, "70")  # Значення за замовчуванням

# 3. Блок введення РОСТУ
frame_height = tk.Frame(root, bg="#f5f6fa")
frame_height.pack(pady=5)

label_height = tk.Label(frame_height, text="Ріст (см або м):", font=("Arial", 11), bg="#f5f6fa", width=12, anchor="w")
label_height.pack(side=tk.LEFT)

entry_height = tk.Entry(frame_height, font=("Arial", 11), width=10, bd=2, relief="groove")
entry_height.pack(side=tk.LEFT)
entry_height.insert(0, "1.75")  # Значення за замовчуванням

# 4. Кнопка розрахунку
btn_calculate = tk.Button(root, text="Розрахувати", font=("Arial", 11, "bold"), bg="#9c88ff", fg="white",
                          activebackground="#8c7ae6", activeforeground="white", width=15, command=calculate_bmi)
btn_calculate.pack(pady=15)

# 5. Блок виведення РЕЗУЛЬТАТІВ
frame_results = tk.Frame(root, bg="#f5f6fa")
frame_results.pack(pady=10)

label_res_text = tk.Label(frame_results, text="Ваш індекс ІМТ:", font=("Arial", 11), bg="#f5f6fa")
label_res_text.grid(row=0, column=0, sticky="w", padx=5)

label_result_value = tk.Label(frame_results, text="0.00", font=("Arial", 12, "bold"), bg="#f5f6fa", fg="#718093")
label_result_value.grid(row=0, column=1, sticky="w", padx=5)

label_cat_text = tk.Label(frame_results, text="Категорія:", font=("Arial", 11), bg="#f5f6fa")
label_cat_text.grid(row=1, column=0, sticky="w", padx=5, pady=5)

label_category_value = tk.Label(frame_results, text="Не розраховано", font=("Arial", 11, "bold"), bg="#f5f6fa",
                                fg="#718093")
label_category_value.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Запуск головного циклу обробки подій вікна (вікно буде відкритим, поки ми його не закриємо)
root.mainloop()
