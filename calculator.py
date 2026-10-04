# Interactive Calculator & Unit Converter
# InternCircle Python Internship - Task 2


def calculator():
    print("\n========== BASIC CALCULATOR ==========")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("❌ Error: Cannot divide by zero!")
                    continue
                result = num1 / num2

            else:
                print("❌ Invalid operator! Please use +, -, * or /.")
                continue

            print("--------------------------------")
            print("✅ Result:", result)
            print("--------------------------------")
            break

        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")


def unit_converter():
    print("\n========== UNIT CONVERTER ==========")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    while True:
        choice = input("Choose an option (1 or 2): ")

        try:
            value = float(input("Enter value: "))

            if choice == "1":
                miles = value * 0.621371

                print("--------------------------------")
                print(f"✅ {value} kilometers = {miles:.2f} miles")
                print("--------------------------------")
                break

            elif choice == "2":
                fahrenheit = (value * 9 / 5) + 32

                print("--------------------------------")
                print(f"✅ {value}°C = {fahrenheit:.2f}°F")
                print("--------------------------------")
                break

            else:
                print("❌ Invalid choice! Please enter 1 or 2.")

        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def main():
    while True:
        print("\n")
        print("==============================================")
        print("  INTERACTIVE CALCULATOR & UNIT CONVERTER")
        print("==============================================")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Exit")
        print("==============================================")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            unit_converter()

        elif choice == "3":
            print("\nThank you for using the program! 👋")
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select 1, 2 or 3.")


# Start the program
if __name__ == "__main__":
    main()