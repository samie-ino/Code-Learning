def divi():
    num1 = int(input("What is your first number?"))
    num2 = int(input("What is your second number?"))
    try:
        result = num1/num2
        print(result)
    except ZeroDivisionError:
        print("This will be Undefined, You can't divide by 0")
divi()