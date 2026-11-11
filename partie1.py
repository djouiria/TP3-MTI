
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)


class OrderPrinter:
    def print_order(self, order):
        print("Order details:")
        for item in order.items:
            print(f"{item['name']}: ${item['price']}")


class OrderRepository:
    def save_to_db(self, order):
        print("Saving order to database...")


# Main call to test the code
if __name__ == '__main__':
    products = [
        {"name": "fruit", "price": 20},
        {"name": "vegetables", "price": 70},
        {"name": "Bread", "price": 15},
        {"name": "Meat", "price": 1500},
    ]

    my_order = Order(products)

    total = my_order.calculate_total()
    print("Total order:", total, "$")

    printer = OrderPrinter()
    printer.print_order(my_order)

    repository = OrderRepository()
    repository.save_to_db(my_order)


