#kaggle reference
from random import choice

shopping_list = ['bread', 'tea leaves', 'ketchup', 'rice']
shopping_list.remove('bread')
shopping_list.append('toilet paper')
print(shopping_list)

#application of functions
"""define the shopping list globally so that all your functions can access it"""
shopping_list = ['bread', 'tea leaves', 'Ketchup', 'rice']

def appendlist(item : str):
    shopping_list.append(item.lower())
    print(f"{item} has been added to the shopping list.")

def removelist(item : str):
    try:
       shopping_list.remove(item.lower())
       print(f"{item} has been removed from the shopping list.")

    except ValueError:
       print(f"{item} is not in the shopping list.")


def displaylist():
    if not shopping_list:
        print("Your Shopping list is empty.")
    else:
        print("\n---Current shopping list:---")
        for index, item in enumerate(shopping_list):
            print(f"{index}: {item}")
            print("-----------\n")

def main():
    while True:
        print("1.Add Item")
        print("2.Remove Item")
        print("3. Display List")
        print("4. Exit")

        choice = int(input("Enter your choice(1-4):"))
        if choice == 1:
            item = input("Enter item to add:")
            appendlist(item)
        elif choice == 2:
            item = input("Enter item to remove:")
            removelist(item)
        elif choice == 3:
            displaylist()
        elif choice == 4:
            print("Thank you for using my programme.")
            break
        else:
            print("Invalid choice, please choose between 1 and 3.")

if __name__ == "__main__":
    main()
