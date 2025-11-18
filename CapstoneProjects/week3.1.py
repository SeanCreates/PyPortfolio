#function for the largest of three numbers
def largestnumber(num1 , num2 , num3):
    if num1 >num2 and num1 > num3:
        return num1
    elif num2 >num1 and num2 >num3:
        return num2
    else:
        return num3

def main():
    print("Largest Number of Three")
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter your second number:"))
        num3 = int(input("Enter your third number:"))

        largest = largestnumber(num1, num2, num3)
        print(f"The largest number is {largest}")
    except ValueError:
        print("Your input is invalid.")

if __name__ == "__main__":
    main()

"""with trial cases"""
def main():
    print("Largest Number of Three")

    result1 = largestnumber(13, 17, 4)
    print(f"The largest number is {result1}")

    result2 = largestnumber(18, 17, 30)
    print(f"The largest number is {result2}")

if __name__ == "__main__":
    main()


