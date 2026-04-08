from color import Color
from point import Point
from shape import Shape
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name='ASquare', location=Point(), color=Color.RED, side: float = 300):
        super().__init__(name, location, color, side, side)

    @property
    def side(self) -> float:
        return self.width  # width ja height ovat samat

    @side.setter
    def side(self, value: float) -> None:
        self.width = self.height = value

    def __str__(self):
        return f"{super().__str__()} with side {self.side}"


if __name__ == "__main__":
    s: Shape = Square()
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
