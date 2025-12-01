#division by zero and valueerror in input
def safe_divide():
    """Prompts the user to input values and handles the errors"""
    while True:
        try:
            numerator_str = input("Enter Your Numerator:")
            denominator_str = input("Enter Your Denominator:")

            numerator = float(numerator_str)
            denominator = float(denominator_str)

            result = numerator / denominator

        except ValueError:
            print("Please input numerical values only")
        except ZeroDivisionError:
            print("Zero Division Error: cannot divide by zero")

        else:
            print(f"The answer is {result}")

safe_divide()



