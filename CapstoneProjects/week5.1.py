import math
def calculate_square_root():
    while True:
        try:
            input_str = "input a non-negative number:"
            number = float(input(input_str))

            if number < 0:
                print("Math Domain Error:The square root of a negative number is complex/invalid.")

            result = math.sqrt(number)
            print(f"The square root of {number}is {result}")

        except ValueError:
            print("only numerical values are allowed.")
        except Exception as e:
            print(f"An unexpected error {e} occured ")
        else :
            break

calculate_square_root()