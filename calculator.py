def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Ой, нельзя делить на ноль!"
    return x / y


def calculator():
    print("Калькулятор")
    while True:
        print("\nВыбери действие:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выйти")

        choice = input("Твой выбор: ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            print("Пока, милый!")
            break
        else:
            print("Неправильный выбор. Попробуй еще раз!")


if __name__ == "__main__":
    calculator()
