from product import Product


class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        if not isinstance(product, Product):
            raise TypeError("Inventory accepts Product subclasses only.")
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id().upper() == product_id.strip().upper():
                return product
        return None

    def find_product(self, product_id: str) -> Product | None:
        return self.search_product(product_id)

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    @property
    def products(self) -> list[Product]:
        return self.__products.copy()

    def display_all_products(self) -> None:
        self.display_all()

    def display_all(self) -> None:
        print("\nCurrent Inventory\n" + "-" * 48)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def to_list(self) -> list[dict]:
        return [product.to_dict() for product in self.__products]
