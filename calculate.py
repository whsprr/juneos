def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Simple Python Calculator")
print("------------------------")

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Ok we will do something else.")
        print("------------------------")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")

    print("------------------------")
