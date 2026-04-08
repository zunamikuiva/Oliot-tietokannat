from product import Product


class MenuProduct:

    def __init__(self):
        pass

    def showOptions(self):

        print("Options:")
        print("1 - Add product")
        print("2 - Show products")
        print("0 - Exit")

    def askChoice(self) -> int:

        return int(input("Your choice: "))

    def run(self) -> None:

        while True:

            self.showOptions()

            choice = self.askChoice()

            if choice == 1:
                self.addProduct()

            elif choice == 2:
                self.showProducts()

            elif choice == 0:
                break

    def addProduct(self) -> None:

        product = Product.createProduct()

        print("Adding product...")

        product.insertDB()

        print("Product added!")
        print()

    def showProducts(self) -> None:

        products = Product.queryProducts([])

        print("No., Manufacturer, Brand, Cost, Price")

        for i, p in enumerate(products, start=1):

            print(f"{i}, {p.manufacturer}, {p.brand}, {p.cost}, {p.price}")
        print()