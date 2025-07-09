class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class DiscountCalculator:
    def calculate_discount(self, book, discount_percentage):
        return book.price * (1 - discount_percentage / 100)


book = Book("Python Basics", "John Doe", 40)
calculator = DiscountCalculator()
print("Preço com desconto:", calculator.calculate_discount(book, 10))
