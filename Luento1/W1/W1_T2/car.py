class Car:
    def __init__(self, color: str):
        self.color = color
        self.engine_on = False

    def start(self) -> None:
        if not self.engine_on:
            self.engine_on = True
            print(f"{self.color} car started.")
        else:
            print(f"{self.color} is already running.")
