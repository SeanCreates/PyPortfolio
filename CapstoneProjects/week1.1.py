#Syntax

# 1. Import necessary libraries (future-proofing)
import datetime


# 2. Define a function for robust user input with error handling
def get_user_age() -> int:
    """Prompts the user for their age and ensures it's a valid integer."""
    global age_str
    while True:
        try:
            age_str = input("Please enter your current age: ")
            age = int(age_str)
            if 0 < age < 120:
                return age
            else:
                print("Error: Please enter a realistic age.")
        except ValueError:
            print(f"Error: '{age_str}' is not a valid number. Please try again.")


# 3. Main program logic
def main():
    """Main function to run the user profile generator."""
    print("--- Welcome to the User Profile Generator ---")

    # Get user input
    user_name = input("Please enter your name: ")
    user_age = get_user_age()

    # 4. Perform a calculation
    current_year = datetime.date.today().year
    birth_year_estimate = current_year - user_age

    # 5. Produce formatted output using an f-string
    summary = (f"\n--- User Profile Summary ---\n"
               f"Name: {user_name.title()}\n"
               f"Age: {user_age}\n"
               f"Estimated Birth Year: {birth_year_estimate}\n")

    print(summary)


# 6. Entry point of the script
if __name__ == "__main__":
    main()