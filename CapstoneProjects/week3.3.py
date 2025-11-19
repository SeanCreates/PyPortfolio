#Sets are mutable, unordered and have unique elements
#Sets are useful in Recommendation engines, Detecting Duplicates and finding unique elements.
def find_common_elements(set_a : set, set_b: set) -> set:
    """Calculates the common elements, the intersection, of two sets"""
    common_elements = set_a.intersection(set_b)
    return common_elements
"""You can either use '&' or 'intersection' """
#common_elements=set_a & set_b

def main():
    print("Set Intersection")
    """Initialize the two sets instead of asking for input"""
    set_a = {1,2,3,4,5,6}
    set_b = {1,3,5,7,8}
    print(f"set 1: {set_a}")
    print(f"set 2: {set_b}")

    common = find_common_elements(set_a, set_b)
    print(f"Intersection is {common}")

    if not common:
        print("No set intersection.")


if __name__ == "__main__" :
    main()


