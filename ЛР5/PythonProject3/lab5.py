# =======================================================
# Лабораторна робота №5. Регулярні вирази (Валідація даних)
# Студент: Аль-Газалі Султан, Група: {З-31}В, Варіант: 1
# =======================================================

import re


def validate_email(email):
    """Перевірка коректності Email за допомогою регулярного виразу."""
    # Шаблон: текст @ текст . текст(від 2 до 4 символів)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if re.match(pattern, email):
        return True
    return False


def find_numbers(text):
    """Пошук усіх цілих чисел у тексті."""
    pattern = r'\d+'
    return re.findall(pattern, text)


def main():
    print("--- Тестування регулярних виразів ---\n")

    # Частина 1: Валідація Email
    emails_to_test = ["sultan.al@univer.edu", "wrong_email@com", "test@domain.com", "invalid@.net"]

    print("Перевірка Email-адрес:")
    for email in emails_to_test:
        status = "Коректний" if validate_email(email) else "НЕкоректний"
        print(f"- {email}: {status}")

    # Частина 2: Пошук чисел у тексті
    sample_text = "Султан здав 3 лабораторні, залишилось ще 5 робіт до 2026 року."
    print(f"\nАналіз тексту: \"{sample_text}\"")
    numbers = find_numbers(sample_text)
    print(f"Знайдені числа у тексті: {numbers}")


if __name__ == "__main__":
    main()
