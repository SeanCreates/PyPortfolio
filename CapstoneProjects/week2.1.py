#Data Types & Operators
#Collections: Lists are ordered and mutable; Tuples are ordered and immutable; Dictionaries are immutable and unordered
#to enhance modularity, we will use multiple functions


#function one
def calculate_area(length, width) -> float:
    return length * width
"""the function calculates the area using the parameters length and width and formula A=l*w first"""

#function two
def compare_area(area1, area2):
    if area1 > area2:
        print("The area for shape one is greater than the area for shape two")
    elif area2 > area1:
        print("The aread for shape two is greater than the area for shape one")
    else:
        print("Both shapes have the same area")
"""the function compares the areas for the two shapes"""

#function three
#The main logic: for the orchestration and input
def main():
    print("Area Calculation and Comparison")

"""The Input for the length and width"""
try:
    length1 = float(input("Enter the length of your first shape:"))
    width1 = float(input("Enter the width of your first shape:"))

    length2 = float(input("Enter the length of your second shape:"))
    width2 = float(input("Enter the width of your second shape:"))

except ValueError:
    print("\n Invalid input, please enter numeric input")



area_shape1 = calculate_area( length1, width1)
area_shape2 = calculate_area( length2, width2)

print(f"\nResults")
print(f"Area of shape1: {area_shape1: ,.2f} sq units")
print(f"Area of shape2: {area_shape2: ,.2f} sq units")

compare_area(area_shape1, area_shape2)
print("-----------")

if __name__ == "__main__":
    main()