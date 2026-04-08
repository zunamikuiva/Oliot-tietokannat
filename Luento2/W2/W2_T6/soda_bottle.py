class SodaBottle:
    def __init__(self, brand: str, volume: float):
        self.brand = brand
        self.volume = volume

    def serialize(self) -> str:
        return f"{self.brand};{self.volume}"

    @staticmethod
    def deserialize(row: str):
        brand, volume = row.split(";")
        return SodaBottle(brand, float(volume))
