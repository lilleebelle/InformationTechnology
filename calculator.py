print("Welcome to the calculator, please input your 2 numbers and operator (e.g. *, /, +, -) when prompted")


def restart():

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    op = input("Enter the operator: ")

    if op == "*":
        ans = num1 * num2
        print(num1, op, num2, "=", ans)

    elif op == "/":
        ans = num1 / num2
        print(num1, op, num2, "=", ans)

    elif op == "+":
        ans = num1 + num2
        print(num1, op, num2, "=", ans)

    elif op == "-":
        ans = num1 - num2
        print(num1, op, num2, "=", ans)

    else:
        print("Invalid operator entered")
        restart()


restart()
