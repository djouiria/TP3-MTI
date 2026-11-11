
class Discount:
    def __init__(self, price):
        self.price = price

    def apply_discount(self):
        return self.price


class VIPDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.8  # 20% discount


# New discount for first-time customers
class FirstTimeCustomerDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.9  # 10% discount


if __name__ == '__main__':
    price = 5000

    # VIP customer
    vip_discount = VIPDiscount(price)
    new_price_vip = vip_discount.apply_discount()
    print(f"VIP - Old price: {price}, VIP - New price: {new_price_vip}")

    # Regular customer
    regular_discount = Discount(price)
    new_price_regular = regular_discount.apply_discount()
    print(f"Regular - Old price: {price}, Regular - New price: {new_price_regular}")

    # First-time customer
    first_time_discount = FirstTimeCustomerDiscount(price)
    new_price_first_time = first_time_discount.apply_discount()
    print(f"First-time customer - Old price: {price}, First-time customer - New price: {new_price_first_time}")
