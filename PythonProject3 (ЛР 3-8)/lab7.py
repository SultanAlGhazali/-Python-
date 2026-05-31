"""
Лабораторна робота №7 (Варіант 1)
Тема: Створення мережевих застосунків та чат-ботів у мові Python
Мета: Ознайомитися з архітектурою створення чат-ботів та розробити ехо-бота для Telegram.
"""

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

# Встав сюди токен, який ти отримав від @BotFather в Telegram
BOT_TOKEN = "8666592668:AAFO0FFQKPMZkTJBjuvcyCOKl2EaH5x2O2U"

# Ініціалізуємо об'єкти бота та диспетчера керування подіями
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 1. Обробник головної команди /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    """Спрацьовує, коли користувач вперше запускає бота або пише /start"""
    user_name = message.from_user.full_name
    await message.answer(
        f"Привіт, {user_name}! 👋\n"
        f"Я чат-бот, створений у межах Лабораторної роботи №7.\n"
        f"Напиши мені щось, і я повторю, або використай команду /help."
    )

# 2. Обробник допоміжної команди /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Спрацьовує на команду /help"""
    await message.answer(
        "**Доступні команди:**\n"
        "/start — Перезапустити бота\n"
        "/help — Отримати довідку про роботу"
    )

# 3. Обробник будь-яких текстових повідомлень (Ехо-функція)
@dp.message()
async def echo_handler(message: types.Message):
    """Дзеркально повертає користувачу надісланий текст"""
    # Додаємо невелике форматування для наочності
    await message.answer(f"🗣 Ви сказали: {message.text}")


# Головна асинхронна функція запуску бота
async def main():
    print("Бот успішно запущений і готовий до роботи! Натисніть Ctrl+C для зупинки.")
    # Запускаємо процес безперервного опитування сервера Telegram на наявність нових повідомлень
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Оскільки aiogram асинхронний, запускаємо його через подієвий цикл asyncio
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот зупинений.")
