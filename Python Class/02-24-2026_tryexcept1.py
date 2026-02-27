def divi():
    num1 = int(input("What is your first number?"))
    num2 = int(input("What is your second number?"))
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("This will be Undefined")
divi()