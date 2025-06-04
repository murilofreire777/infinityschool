class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError()

class CardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processando pagamento com cartão: {amount}")

class PaypalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processando pagamento com PayPal: {amount}")

payment = CardPayment()
payment.process_payment(50)
