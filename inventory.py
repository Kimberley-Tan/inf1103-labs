from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Inventory accepts Product subclasses only.")
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id().upper() == product_id.strip().upper():
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory\n" + "-" * 48)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def to_list(self):
        return [product.to_dict() for product in self.__products]
