from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class FileLogger(Logger):
    def log(self, message: str):
        print(f"Log em arquivo: {message}")

class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def run(self):
        self.logger.log("Aplicação está rodando")

# Usando a aplicação com verificação de tipos
app = Application(FileLogger())
app.run()
