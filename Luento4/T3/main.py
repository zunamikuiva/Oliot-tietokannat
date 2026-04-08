from db_conn import DB_CONN
from menu_product import MenuProduct


class Main:

    PRODUCT_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        manufacturer VARCHAR(255) NOT NULL,
        brand VARCHAR(255) NOT NULL,
        cost REAL NOT NULL,
        price REAL NOT NULL
    );
    """

    def __init__(self):
        print("Program starting.")

        cursor = DB_CONN.cursor()
        cursor.execute(Main.PRODUCT_TABLE_STATEMENT)
        DB_CONN.commit()
        cursor.close()

        menu = MenuProduct()
        menu.run()

        DB_CONN.close()

        print("Program ending.")


if __name__ == "__main__":
    Main()