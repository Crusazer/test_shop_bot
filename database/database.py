import sqlite3
from settings import settings
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    description: str
    photo_id: str
    price: int
    count: int


class DataBase:
    def __init__(self, path: str):
        self._connection = sqlite3.connect(path)
        self._cursor = self._connection.cursor()
        self._create_goods_table()

    def __delattr__(self, item):
        self._cursor.close()
        self._connection.commit()

    def _create_goods_table(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS goods(
        id INT PRIMARY KEY,
        name TEXT,
        description TEXT,
        photo_id TEXT,
        price INT,
        count INT);        
        """)

    def add_product(self, product: Product):
        value = [product.id, product.name, product.description, product.photo_id, product.price, product.count]
        self._cursor.execute(f"INSERT INTO goods VALUES (?, ?, ?, ?, ?, ?)", value)
        self._connection.commit()

    def get_product(self, product_id: int) -> Product:
        self._cursor.execute(f"SELECT * FROM {settings.GOODS} WHERE id = ?", (product_id,))
        values = self._cursor.fetchone()
        return Product(*values)

    def get_goods(self, start_number, numbers: int) -> list:
        self._cursor.execute(f"SELECT * FROM {settings.GOODS} WHERE id > {start_number} LIMIT {numbers}")
        values_list = self._cursor.fetchall()
        return [Product(*values) for values in values_list]

    def get_all_goods(self) -> list:
        """ Get all goods from the table """
        self._cursor.execute(f"SELECT * FROM {settings.GOODS}")
        values_list = self._cursor.fetchall()
        return [Product(*values) for values in values_list]

    def delete_product(self, product_id):
        """ Delete the product in table on id """
        self._cursor.execute(f"DELETE FROM {settings.GOODS} WHERE id = ?", (product_id,))
        self._connection.commit()

    def get_last_product_id(self) -> int:
        """
        Return the id of last product.
        If the table is empty then return 0.
        """
        self._cursor.execute(f"SELECT * FROM {settings.GOODS} ORDER BY id DESC LIMIT 1")
        values = self._cursor.fetchone()
        if values:
            return values[0]
        else:
            return 0


# Import this object to use database
db = DataBase(f"{settings.PATH_DB_GOODS}")
