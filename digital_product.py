import math
from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        if not math.isfinite(float(download_size)) or float(download_size) < 0:
            raise ValueError("Download size must be a non-negative finite number.")
        self.__download_size = float(download_size)

    def display_information(self):
        super().display_information()
        print(f"  Type: Digital | Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        return "Delivered digitally via download."

    def to_dict(self):
        data = super().to_dict()
        data.update({"type": "digital", "download_size": self.__download_size})
        return data
