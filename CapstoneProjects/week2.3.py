#prints the multiplication table of a number
#function 1
def multiplicationtable(number : int):
    print(f"\n Multiplication table for {number} is:")
    for i in range(1, number + 1):
        result = number * i
        print(f"{number} * {i:02} = {result}")

#main function with logic and user input
def main():
    print("Multiplication table")
    try:
        user_input = input("Please enter the number for the multiplication table:")
        base_num = int(user_input)
        multiplicationtable(base_num)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()

