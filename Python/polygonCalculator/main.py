import math

class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height

    def set_width(self, value):
        self._width = value

    def set_height(self, value):
        self._height = value
    
    def get_area(self):
        return self._width * self._height 

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        return math.sqrt(self._width**2 + self._height**2)

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        
        result = ""
        for i in range(self._height):
            result += "*" * self._width + "\n"
        return result
    
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
        
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self._width = side
        self._height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self._width})"



if __name__ == "__main__":
    rectangle = Rectangle(3, 6)
    print(rectangle)
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
    print(rectangle.get_diagonal())
    print(rectangle.get_picture())
    print(rectangle.get_amount_inside(Rectangle(1,2)))

    square = Square(3)
    print(square)
    print(square.get_area())
    print(square.get_perimeter())
    print(square.get_diagonal())
    print(square.get_picture())
    