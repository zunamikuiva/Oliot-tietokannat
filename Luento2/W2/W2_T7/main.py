from training_session import TrainingSession


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Reading training log...")

        sessions = []
        total_time = 0

        file = open("input_1.txt", "r")
        for line in file:
            session = TrainingSession.from_string(line)
            sessions.append(session)
            total_time += session.duration
        file.close()

        print("Training sessions:")
        for s in sessions:
            print(f"{s.sport} - {s.duration} min")

        print(f"Total training time: {total_time} minutes")
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
