class EmailSender:
    def send(self, message):
        print(f"Enviando e-mail: {message}")

class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

email_sender = EmailSender()
service = NotificationService(email_sender)
service.notify("Olá, mundo!")
