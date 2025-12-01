#Store and Retrieve Students' Grades
#dictionaries are defined as objects with the data type 'dict'

this_dict = {
    "Seanice" : "90%",
    "Paris"   : "80%",
    "Sara"    : "78%"
}
print(this_dict)
print(len(this_dict))
"""<class dict >"""
print(type(this_dict))

#dict constructor
this_dict = dict(name = "seanice" , age = 20, country = "Canada")
print(this_dict)
x = this_dict.keys()
print(x)

#Programme that stores and retrieves grades
"""Initialize the global dictionary"""
student_grades = {}
def add_grade(name : str, grade : float):
    """Adds or Updates a student name or grade"""
    student_grades[name.title()] = grade
    print(f"{grade} has been recorded for {name.title()}")

def retrieve_grade(name: str):
    """Retrieves a grade for a student, handling cases where the student is not found"""
    student_name = name.title()
    #use the in operator to check if the key exists before allowing access
    if student_name in student_grades:
        grade = student_grades[student_name]
        print(f"{student_name}'s grade is: {grade}")
    else:
        #if the key does not exist, present user feedback
        print(f"Error : {student_name} is not found in the records.")

def main():
    print("Welcome To The Grade Management system")
    #initial data entry examples
    add_grade("Seanice", 90)
    add_grade("Paris", 80)
    add_grade("Sara", 70)

    print("Retrieving Grades")
    retrieve_grade("Seanice")
    retrieve_grade("Paris")
    retrieve_grade("Charlie")

if __name__ == "__main__":
    main()



