from db_conn import DB_CONN


class Product:

    def __init__(self, manufacturer: str, brand: str, cost: float, price: float):

        self.manufacturer = manufacturer
        self.brand = brand
        self.cost = cost
        self.price = price

    @staticmethod
    def createProduct() -> 'Product':

        print("Insert product details below:")

        manufacturer = input("- Insert manufacturer: ")
        brand = input("- Insert brand: ")
        cost = float(input("- Insert cost: "))
        price = float(input("- Insert price: "))

        return Product(manufacturer, brand, cost, price)

    def insertDB(self) -> None:

        cursor = DB_CONN.cursor()

        cursor.execute(
            """
            INSERT INTO product(manufacturer, brand, cost, price)
            VALUES(?,?,?,?)
            """,
            (self.manufacturer,
             self.brand,
             self.cost,
             self.price)
        )

        DB_CONN.commit()

        cursor.close()

    @staticmethod
    def queryProducts(products: 'list[Product]' = []) -> 'list[Product]':

        cursor = DB_CONN.cursor()

        cursor.execute("SELECT manufacturer, brand, cost, price FROM product")

        rows = cursor.fetchall()

        for row in rows:

            product = Product(row[0], row[1], row[2], row[3])

            products.append(product)

        cursor.close()

        return products