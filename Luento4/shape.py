from abc import ABC, abstractmethod
from point import Point
from color import Color

class Shape(ABC):
    def __init__(self, name:str = 'ASHape', location:Point = Point(), color:Color = Color.NONE):
        self.name = name
        self.location = location
        self.color = color


    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value:str) -> None:
        self.__name = value

    @property
    def location(self) -> Point:
        return self.__location
    
    @location.setter
    def location(self, value:Point):
        self.__location = value

    @property
    def color(self) -> Color:
        return self.__color
    
    @color.setter
    def color(self, value: Color) -> None:
        self.__color = value

    def __str__(self):
        return f"{self.name}, color {self.color} at {self.location}"
    
    @abstractmethod
    def area(self) -> float:
        #raise NotImplementedError("Subclasses should calculate the area...")
        return 0

    @abstractmethod
    def perimeter(self) -> float:
        #raise NotImplementedError("Sublclasses should calculate the perimeter...")
        return 0
    
if __name__ == "__main__":
    s:Shape = Shape("MyShape", Point(100,200), Color.BLUE) #error!
    print(s)
    #print("Area: ", s.area())
    #print("Perimeter: ", s.perimeter())