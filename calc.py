def calculator():
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