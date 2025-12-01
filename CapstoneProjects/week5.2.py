import datetime
class Car:
    """Represents a car with basic and essential attributes"""
    #The constructor method, initialization
    def __init__(self, make, model, year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    #method1, display information
    def display_info(self):
        print("car Information")
        print(f"Make: {self.make}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        print(f"color: {self.color}")

     #calculate car age
    def age(self) -> int:
        current_year = datetime.date.today().year
        return current_year - self.year

def main():
    my_car = Car("Mercedes", "GLE" , 2005, "Black")
    print(f"Created a {my_car.color} {my_car.make}")
    my_car.display_info()

    car_age = my_car.age()
    print(f"This car is {car_age} years old")

if __name__ == "__main__":
    main()




