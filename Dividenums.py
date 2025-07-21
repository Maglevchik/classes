class NegativeNumberError(Exception):
    pass

def sqrt(num):
    try:
        if num < 0:  # Проверяем, является ли число отрицательным
            raise NegativeNumberError("Невозможно вычислить квадратный корень из отрицательного числа.")
        else:
            sqrtt = num ** 0.5
            return sqrtt
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Операция завершена.")

def get_number_from_user(prompt):
    while True:
        try:
            num_str = input(prompt)
            number = float(num_str)
            return number
        except ValueError:
            print("Ошибка: Некорректный ввод данных! Пожалуйста, вводите только числа.")
        except KeyboardInterrupt:
            print("Ошибка: Вы наверно нажали сочетание клавиш!")

def divide_numbers(n1,n2):
    try:
        div = n1 / n2
        return div
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
    finally:
        print("Операция завершена.")

num1 = get_number_from_user("Введите первое число: ")
num2 = get_number_from_user("Введите второе число: ")
num3 = get_number_from_user("Введите третье число, чтоб извлечь из него квадратный корень: ")

divide = divide_numbers(num1,num2)
print(f'Деление 1-го на 2-е: {divide}')

numsqrt = sqrt(num3)
print(f'Извлечение кв. корня из 3-го: {numsqrt}')