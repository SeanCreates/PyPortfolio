#Conditionals
#Function one to check if the number is positive, negative or just zero
def check_number( number : float):
    if number < 0:
        print(f"The {number} is negative")
    elif number > 0:
        print(f"The {number} is positive")
    else:
        print(f"The {number} is zero")

    return

#The main function where the 'heavy lifting' and logic
def main():
    print("Number Classifier")
    try:
        user_input = input("Please enter a number:")
        num = float(user_input)
        check_number(num)
    except ValueError:
        print(f" {user_input} is not a number. Please try again")

if __name__ == "__main__":
    main()
