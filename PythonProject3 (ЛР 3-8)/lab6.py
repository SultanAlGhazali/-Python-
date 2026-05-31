"""
Лабораторна робота №6 (Варіант 1)
Тема: Збір даних з веб-документів за допомогою мови Python
Мета: Навчитися одержувати дані з HTML-сторінок та здійснювати їх аналіз за допомогою requests та BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


def scrape_hacker_news():
    """Функція для парсингу заголовків та посилань з першої сторінки Hacker News"""
    url = "https://ycombinator.com"

    # Додаємо заголовок User-Agent, щоб сервер розумів, що запит йде від браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Надсилання GET-запиту до {url}...")

    try:
        # Виконуємо HTTP GET-запит
        response = requests.get(url, headers=headers, timeout=10)

        # Перевіряємо статус відповіді (200 означає успіх)
        if response.status_code == 200:
            print("HTTP-запит успішний! Починаємо аналіз HTML-структури...\n")

            # Передаємо HTML-код сторінки в парсер BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # На сайті Hacker News кожен заголовок новини лежить у тезі <span> з класом 'titleline'
            titles_tags = soup.find_all("span", class_="titleline")

            print(f"Знайдено новин на сторінці: {len(titles_tags)}\n")
            print(f"{'№':<3} | {'Заголовок новини':<60} | Посилання")
            print("-" * 100)

            # Ітеруємося по знайдених елементах (виведемо перші 15 для демонстрації)
            for index, tag in enumerate(titles_tags[:15], 1):
                # Всередині span.titleline шукаємо тег <a>, який містить посилання та текст
                link_tag = tag.find("a")
                if link_tag:
                    title_text = link_tag.text
                    link_url = link_tag.get("href")

                    # Форматуємо довгі заголовки, щоб виведення було красивим
                    short_title = title_text if len(title_text) <= 57 else title_text[:54] + "..."
                    print(f"{index:<3} | {short_title:<60} | {link_url}")

        else:
            print(f"Помилка сервера. Статус-код: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка при підключенні до мережі: {e}")


if __name__ == "__main__":
    print("=== ЛАБОРАТОРНА РОБОТА №6: ВЕБ-ПАРСИНГ ТА ЗБІР ДАНИХ ===")
    scrape_hacker_news()
