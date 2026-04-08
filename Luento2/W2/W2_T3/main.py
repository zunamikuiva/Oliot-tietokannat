class Main:
    def __init__(self) -> None:
        print("Program starting.")

        while True:
            print("Menu:")
            print("1 - Add bottle")
            print("2 - Show bottle")
            print("3 - Save bottle")
            print("0 - Exit")
            choice = input("Your choice: ")

            if choice == "1":
                print("'Add bottle' not implemented yet.")
            elif choice == "2":
                print("'Show bottle' not implemented yet.")
            elif choice == "3":
                print("'Save bottle' not implemented yet.")
            elif choice == "0":
                print()
                print("Exiting program.")
                break
            else:
                print("Unknown option, try again.")
            print()

        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
