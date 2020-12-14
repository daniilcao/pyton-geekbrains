def testNumbers(param):
    """Проверка данных на целые числа и деления на 0."""
    try:
        data_res_var = [int(i) for i in param]
        if len(data_res_var) == 2:
            n1, n2 = data_res_var
            try:
                r = n1 / n2
                print(f"Res data {round(r, 1)}")
            except ZeroDivisionError:
                print("Division by zero is not allowed")

    except Exception:
        print("These are not correct numbers")


testNumbers(input("set two numbers with a space:").split())
