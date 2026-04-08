from soda_bottle import SodaBottle


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        bottles = []

        while True:
            print("Menu:")
            print("1 - Add bottle")
            print("2 - Show bottles")
            print("3 - Save bottle")
            print("0 - Exit")
            choice = input("Your choice: ")

            if choice == "1":
                print("Creating soda bottle.")
                brand = input("Insert brand: ")
                volume = float(input("Insert volume: "))
                bottles.append(SodaBottle(brand, volume))

            elif choice == "2":
                print("#### Soda bottles ####")
                for i, b in enumerate(bottles, start=1):
                    print(f"Bottle {i}:")
                    print(f"  brand - {b.brand}")
                    print(f"  volume - {b.volume}")
                print("#### Soda bottles ####")

            elif choice == "3":
                print("Saving soda bottles...")
                rows = [b.serialize() + "\n" for b in bottles]
                content = "".join(rows)
                file = open("inventory.txt", "w")
                file.write(content)
                file.close()
                print("Saving completed!")

            elif choice == "0":
                print()
                print("Exiting program.")
                break

            print()

        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
