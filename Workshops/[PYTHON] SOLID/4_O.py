class PriceCalculator:
    def calculate_price(self, price, discount_strategy):
        return discount_strategy.apply_discount(price)

class NoDiscount:
    def apply_discount(self, price):
        return price

class PercentageDiscount:
    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, price):
        return price * (1 - self.percent / 100)

calculator = PriceCalculator()
print("Preço sem desconto:", calculator.calculate_price(100, NoDiscount()))
print("Preço com desconto:", calculator.calculate_price(100, PercentageDiscount(10)))
