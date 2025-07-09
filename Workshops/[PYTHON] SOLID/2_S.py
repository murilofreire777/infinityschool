class DataReader:
    def read_data(self, source):
        print(f"Lendo dados de {source}")
        return "dados lidos"

class DataWriter:
    def write_data(self, destination, data):
        print(f"Escrevendo {data} em {destination}")

reader = DataReader()
writer = DataWriter()
data = reader.read_data("arquivo.txt")
writer.write_data("arquivo.txt", data)
