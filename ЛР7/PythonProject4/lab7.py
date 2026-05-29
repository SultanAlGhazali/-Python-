# =======================================================
# Лабораторна робота №7. Елементи комп'ютерної графіки
# Студент: Аль-Газалі Султан
# Група: КБ-25з
# Варіант: 1
# =======================================================

import turtle


def draw_axes():
    """Малювання колінеарних осей координат X та Y."""
    turtle.color("black")
    turtle.width(2)

    # Вісь X
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    turtle.goto(300, 0)
    turtle.write("X", font=("Arial", 12, "bold"))

    # Вісь Y
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.goto(0, 300)
    turtle.write("Y", font=("Arial", 12, "bold"))


def draw_parabola():
    """Побудова графіка функції y = x^2 з масштабуванням."""
    turtle.color("blue")
    turtle.width(3)
    turtle.penup()

    # Масштабні коефіцієнти для наочності на екрані
    scale_x = 20
    scale_y = 5

    # Обчислюємо точки графіка від x = -7 до x = 7
    for x_grid in range(-70, 71):
        x = x_grid / 10.0  # Крок 0.1 для плавності лінії
        y = x ** 2

        # Перераховуємо в екранні координати
        screen_x = x * scale_x
        screen_y = y * scale_y

        turtle.goto(screen_x, screen_y)
        turtle.pendown()


def main():
    # Налаштування вікна відображення
    turtle.title("Лабораторна робота №7 — Графік y = x^2")
    turtle.setup(width=800, height=600)
    turtle.speed(0)  # Максимальна швидкість малювання

    print("Малювання графіка функції... Зачекайте або подивіться у вікно Turtle.")

    draw_axes()
    draw_parabola()

    # Текстовий підпис на екрані
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.color("darkgreen")
    turtle.write("Графік функції y = x² (Варіант 1)", font=("Arial", 14, "italic"))

    # Залишає вікно відкритим після завершення малювання
    turtle.done()


if __name__ == "__main__":
    main()
