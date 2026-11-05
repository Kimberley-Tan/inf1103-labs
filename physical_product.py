import math
from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        if not math.isfinite(float(weight)) or float(weight) < 0:
            raise ValueError("Weight must be a non-negative finite number.")
        self.__weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"  Type: Physical | Weight: {self.__weight:.2f} kg | Shipping: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return 3.0 + 2.0 * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data.update({"type": "physical", "weight": self.__weight})
        return data
