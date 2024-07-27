import math


def g(x):
    return math.exp(-x / 2)


def main():
    x = float(input("Введите начальное значение x0: "))
    e = float(input("Введите точность e: "))

    while True:
        x1 = g(x)
        d = abs(x1 - x)
        print(f"x = {x1}, погрешность d = {d}")

        if d < e:
            break

        x = x1

    print(f"Решение уравнения: x = {x1}")


if __name__ == "__main__":
    main()
