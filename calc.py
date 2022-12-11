def calculator():
    print("Веселов Олег Русланович ИКБО-20-19 Поток 2")
    print("Введите первое число:")
    x = float(input())
    print("Введите второе число:")
    y = float(input())
    print("Введите оператор:")
    oper = input()

    if oper == "+":
        print("Результат: "+str(x+y))
    elif oper == "-":
        print("Результат: "+str(x-y))
    elif oper == "/":
        print("Результат: "+str(x/y))
    elif oper == "*":
        print("Результат: "+str(x*y))

calculator()