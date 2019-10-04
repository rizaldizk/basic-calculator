num1 = float(input("Enter number here: "))
op = input("Enter operator here: ")
num2 = float(input("Enter number here: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("error")