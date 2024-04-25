"""
Приложение калькулятор
"""


def calculate():
    """
    Функция запускает работу калькулятора
    :return: строковый результат вычислений
    """

    print("Добро пожаловать в калькулятор!")
    print("В данном калькуляроте работают 4-е функции: сложение '+' , вычитание '-' , умножение '*' , деление '/'.")
    print("Чтобы провести вычисление введите числа и действие (+, -, *, /).")

    flag = False
    answer = ''
    result = 0

    while True:
        result = actions(result, flag, answer)
        print(f"\nРезультат: {result}")
        answer = input("\nЕсли продолжаем считать дальше, то введите действие (+, -, *, /)."
                       "\nЕсли хотите начать с начала введите 'старт'."
                       "\nЕсли хотите закончить, то напишите 'стоп'.\n"
                       "\nВведите действие (+, -, *, /) или 'старт/стоп': ")

        if answer.lower().strip() == "стоп" or answer.lower().strip() == "stop":
            print(f"\nИтоговый результат: {result}"
                  "\nКалькулятор закрыт!")
            break
        elif answer.lower().strip() == "старт" or answer.lower().strip() == "start":
            print(f"\nИтоговый результат: {result}\n")
            calculate()
            break
        else:
            flag = True
            continue


def valid_num() -> int or float:
    """
    Функция валидирует введенное число
    :return: число типа int или float
    """
    while True:
        try:
            val_ = input("\nВведите число: ")
            if '.' in val_:
                val_ = float(val_)
            else:
                val_ = int(val_)
            return val_
        except ValueError:
            print("Необходимо ввести целое или десятичное число! Например: 7 или 0.02")
            continue


def valid_actions(flag=False, act_=None) -> str:
    """
    Функция проводит валидацию введенного знака вычисления
    :param flag: флаг указывающий, что вычисления продолжаются
    :param act_: введенный знак вычислений
    :return: строковый знак вычисления
    """
    if flag:
        while True:
            if act_ == "+" or act_ == "-" or act_ == "*" or act_ == "/" or act_ == "/":
                return act_
            else:
                print("Необходимо указать одно из действий (+, -, *, /)")
                act_ = input("\nВведите действие (+, -, *, /): ")
                continue
    else:
        while True:
            act_ = input("\nВведите действие (+, -, *, /): ")
            if act_ == "+" or act_ == "-" or act_ == "*" or act_ == "/" or act_ == "/":
                return act_
            else:
                print("Необходимо указать одно из действий (+, -, *, /)")
                continue


def actions(num_=0, flag=False, act_=None) -> int or float:
    """
    Функция проводящая вычислений
    :param num_: полученный результат при первом вычислении
    :param flag: флаг указывающий, что вычисления продолжаются
    :param act_: введенный знак вычислений
    :return: результат вычислений типа int или float
    """
    if flag:
        num_1 = num_
        action = valid_actions(flag, act_)
    else:
        num_1 = valid_num()
        action = valid_actions()
    num_2 = valid_num()
    if action == "+":
        result = num_1 + num_2
    elif action == "-":
        result = num_1 - num_2
    elif action == "*":
        result = num_1 * num_2
    else:
        while True:
            if num_2 == 0:
                print("\nДелить на '0' невозможно."
                      "\nВведите любое число кроме '0'")
                num_2 = valid_num()
                continue
            else:
                break
        result = num_1 / num_2
    return result


if __name__ == '__main__':
    calculate()
