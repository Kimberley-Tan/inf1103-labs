import unittest
from unittest.mock import patch
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from supplier import Supplier
from inventory import Inventory
from order import Order
from order_line import OrderLine
from product_factory import ProductFactory
from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from csv_loader import get_positive_float, load_products


class Lab9Tests(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S01", "ABC Supplies", "abc@example.com")
        self.product = ProductFactory.create("physical", "P01", "Mouse", 25, 10, self.supplier, weight=0.5)

    def test_strategy_and_switch(self):
        order = Order("O01")
        order.add_order_line(self.product, 10)
        self.assertEqual(order.calculate_total(), 250)
        order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225)
        order.set_discount(StudentDiscount())
        self.assertEqual(order.calculate_total(), 237.5)
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_factory(self):
        digital = ProductFactory.create("digital", "D01", "Book", 12, 5, self.supplier, download_size=3)
        self.assertEqual(digital.get_fulfilment_info(), "Delivered digitally via download.")
        with self.assertRaisesRegex(ValueError, "Unknown product type"):
            ProductFactory.create("service", "S01", "Service", 10, 2, self.supplier)

    def test_validation(self):
        for price in (0, -5, float("nan")):
            with self.subTest(price=price), self.assertRaises(ValueError):
                ProductFactory.create("physical", "P02", "Bad", price, 1, self.supplier)
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D02", "Bad", 10, -1, self.supplier)
        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)
        with self.assertRaises(ValueError):
            self.product.update_stock(-1)

    def test_input_retry(self):
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]), patch("sys.stdout", new_callable=StringIO) as out:
            self.assertEqual(get_positive_float("Price: "), 12.5)
        self.assertIn("Please enter a valid number", out.getvalue())
        self.assertIn("Please enter a number greater than zero", out.getvalue())

    def test_csv_load_and_missing(self):
        inventory = Inventory()
        sample = Path(__file__).with_name("products.csv")
        with patch("sys.stdout", new_callable=StringIO) as out:
            load_products(str(sample), inventory, self.supplier)
        self.assertEqual(len(inventory.products), 3)
        self.assertIn("3 products loaded.", out.getvalue())
        self.assertIn("Skipping row 4", out.getvalue())
        self.assertIn("Skipping row 5", out.getvalue())
        with TemporaryDirectory() as directory:
            with patch("sys.stdout", new_callable=StringIO) as out:
                load_products(str(Path(directory) / "missing.csv"), inventory, self.supplier)
            self.assertIn("Products file not found", out.getvalue())
            self.assertIn("Load attempt finished.", out.getvalue())


if __name__ == "__main__":
    unittest.main()
