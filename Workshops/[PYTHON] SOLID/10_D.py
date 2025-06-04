class Logger:
    def log(self, message: str):
        raise NotImplementedError("Subclasses devem implementar este método")

class FileLogger(Logger):
    def log(self, message: str):
        print(f"Log em arquivo: {message}")

class DatabaseLogger(Logger):
    def log(self, message: str):
        print(f"Log no banco de dados: {message}")

class Application:
    def __init__(self, logger: Logger):
        if not isinstance(logger, Logger):
            raise TypeError("logger deve ser uma instância de Logger ou de suas subclasses")
        self.logger = logger

    def run(self):
        self.logger.log("Aplicação está rodando")

# Exemplo de uso:
app = Application(FileLogger())
app.run()
