from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def show_product_details(product):
    product.display_information()
    print(product.get_fulfilment_info())


def main():
    supplier = Supplier("S01", "ABC Supplies", "abc@example.com")
    physical = PhysicalProduct("P01", "Mouse", 20, 10, 0.5, supplier)
    digital = DigitalProduct("D01", "E-book", 12, 20, 5, supplier)
    del supplier
    assert physical.supplier is digital.supplier
    physical.supplier.display_information()
    digital.supplier.display_information()
    inventory_a, inventory_b = Inventory(), Inventory()
    assert inventory_a.add_product(physical)
    assert inventory_a.remove_product("P01")
    assert physical.get_name() == "Mouse"
    assert inventory_b.add_product(physical)
    assert inventory_b.add_product(digital)
    for product in inventory_b.products:
        show_product_details(product)
        product.update_stock(5)
        assert product.get_stock() == 5
    order1, order2 = Order("O01"), Order("O02")
    order1.add_order_line(physical, 2)
    order1.add_order_line(digital, 1)
    order2.add_order_line(physical, 1)
    assert len(order1.order_lines) == 2
    assert order1.order_lines[0] is not order2.order_lines[0]
    assert order1.order_lines[0].product is order2.order_lines[0].product
    assert order1.calculate_total() == 52
    assert order2.calculate_total() == 20
    order1.remove_order_line(1)
    assert order1.calculate_total() == 40
    print("All Lab 8 tests passed.")


if __name__ == "__main__":
    main()
