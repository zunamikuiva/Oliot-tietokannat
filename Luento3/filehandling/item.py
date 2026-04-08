# pure data class to represent an item in the shipping cart
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float

    @staticmethod
    def deserialize(item_string: str) -> 'Item':
        name, price = item_string.srtip().split(';')
        return Item(name, float(price))
    @staticmethod
    def serialize(self) -> str:
        name, price = self.name, self.price