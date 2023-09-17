def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def main():
    print("--------------------SIMPLE PYTHON CALCULATOR--------------------")
    print("Made By :- Rajib Bishal")

    while True:
        print("----------------------------------------------------------------")
        print()
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter operation (1/2/3/4/5): ")

        if choice not in ('1', '2', '3', '4', '5'):
            print("Invalid input")
            main()
            return
        if choice == '5':
            exit()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        print("Result: ", result)

if __name__ == "__main__":
    main()
