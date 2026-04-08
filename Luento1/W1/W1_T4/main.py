from coin_acceptor import CoinAcceptor


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Welcome to coin acceptor program.")
        print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
        print()

        acceptor = CoinAcceptor()

        while True:
            value = float(input("Insert coin(0 return, -1 exit): "))

            if value == -1:
                print("Exiting program.")
                print()
                break

            elif value == 0:
                print("Returning coins...")
                amount, total = acceptor.returnCoins()
                print(f"{amount} coins with {total}€ value returned.")
                print(f"Inserted coins - {acceptor.getAmount()}, value - 0€")
                print()

            else:
                print("Inserting...")
                acceptor.insertCoin(value)
                print(f"Inserted coins - {acceptor.getAmount()}, value - {acceptor.getValue()}€")
                print()

        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
