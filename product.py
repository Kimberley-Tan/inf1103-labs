class Product:
    def __init__(self, product_id, name, price, stock):
        if not str(product_id).strip() or not str(name).strip():
            raise ValueError("Product ID and name cannot be empty.")
        if float(price) < 0 or int(stock) < 0:
            raise ValueError("Price and stock cannot be negative.")
        self.__product_id = str(product_id).strip().upper()
        self.__name = str(name).strip()
        self.__price = float(price)
        self.__stock = int(stock)

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative integer.")
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}
