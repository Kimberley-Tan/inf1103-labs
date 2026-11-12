import math
from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        if not math.isfinite(float(download_size)) or float(download_size) < 0:
            raise ValueError("Download size must be a non-negative finite number.")
        self.__download_size = float(download_size)

    def display_information(self) -> None:
        super().display_information()
        print(f"  Type: Digital | Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally via download."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"type": "digital", "download_size": self.__download_size})
        return data
