class TrainingSession:
    def __init__(self, sport: str, duration: int):
        self.sport = sport
        self.duration = duration

    @staticmethod
    def from_string(row: str):
        sport, duration = row.strip().split(";")
        return TrainingSession(sport, int(duration))
