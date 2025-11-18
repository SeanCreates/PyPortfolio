#a factorial of a number
"""n * (n-1) * (n-2) * ..."""
def factorial(number : int):
    """Calculate the factorial of a positive integer using iteration"""
    #input validation
    if number < 0:
        return "Factorial of negative numbers is not supported."
    if number == 0:
        return 1

    #initialize result accumulator to 1
    """This is like saying:“We are going to multiply a bunch of numbers, 
    so let’s start with 1, because multiplying by 1 doesn’t change anything.”"""

    result = 1

    #iterate from one upto and including the input number
    #range (1, number + 1) iterates from 1,2,3,...,number
    #so let's say the number is 5, the range is (5,5+1)
    for i in range(1, number + 1):
        result *= i

    #Print the calculation steps (for debugging/demonstration)
    print(f"Calculation: {'*' .join(map(str, range(1, number + 1)))}")

    return result


def main():
    try:
        user_input = input("Please enter a non-negative integer: ")
        num = int(user_input)

        factorial_result = factorial(num)

        if isinstance(factorial_result, str):
            print(f" {factorial_result}")
        else:
            print(f"\n The factorial of {num}! is: {factorial_result}")

    except ValueError:
        print(f" Error: '{user_input}' is not a valid integer. Please try again.")


if __name__ == "__main__":
    main()





