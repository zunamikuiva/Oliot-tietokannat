from color import Color
from point import Point
from shape import Shape

class Rectangle(Shape):
    def __init__(self, name = 'ARect', location = Point(), color = Color.BLACK, width:float = 100, height: float = 50):
        super().__init__(name, location, color)
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self.__width
    
    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            self.__width = 10
        else:
            self.__width = value


    @property
    def height(self, value:float) -> None:
        return self.__height
    
    @height.setter
    def height(self, value:float) -> None:
        if value <= 0:
            self.__height = 10
        else:
            self.__height = value

    def __str__(self):
        return f"{super().__str__()}, w: {self.widht} h: {self.height}"
        
    def area(self):
        return self.widht * self.height
    
    def perimeter(self):
        return 2*(self.widht + self.height)
    
if __name__ == "__main__":
    s:Shape = Rectangle()
    print(s)
    print("Area: ", s.area())
    print("Perimeter: ", s.perimeter())