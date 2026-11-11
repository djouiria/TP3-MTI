
class Shape:
    def get_area(self):
        raise NotImplementedError(
            "Must be implemented by the subclass"
        )


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length


# Client code
def print_area(shape):
    print(f"Area: {shape.get_area()}")


# Main call to test the code
if __name__ == '__main__':
    rect = Rectangle(5, 10)
    square = Square(5)

    print("Rectangle:")
    print_area(rect)

    print("Square:")
    print_area(square)
