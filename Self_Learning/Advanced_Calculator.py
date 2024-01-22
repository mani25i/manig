print("###################Advanced Calulator####################")
num1 = float(input("Enter number 1: "))
op = input("Enter operator: ")
num2 = float(input("Enter number 2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")