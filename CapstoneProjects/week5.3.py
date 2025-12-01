class Rectangle:
    def __init__(self, length:float, width:float):
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def display_info(self):
        print(f"length: {self.length}")
        print(f"width: {self.width}")


def main():
    print("Rectangle Area calculator OOP")

    rectangle_r1 = Rectangle(100, 50)
    rectangle_r1.display_info()

    rectangle_r2 = Rectangle( 76, 89)
    rectangle_r2.display_info()

    area_r1 = rectangle_r1.calculate_area()
    print(f"Rectangle R1's area is: {area_r1}")

    area_r2 = rectangle_r2.calculate_area()
    print(f"Rectangle r2's area is: {area_r2}")

if __name__ == "__main__":
    main()
