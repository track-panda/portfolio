
number_1 = int(input("Give me a number.").strip())
operation = input("Give me an operation, such as: + - * / **.").strip()
number_2 = int(input("Give me a another number.").strip())

if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)
elif operation == "**":
    print(number_1 ** number_2)
else:
    print("Error!")