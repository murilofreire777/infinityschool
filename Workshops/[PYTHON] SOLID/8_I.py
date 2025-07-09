class ReportGenerator:
    def generate(self):
        raise NotImplementedError()

class PDFReportGenerator(ReportGenerator):
    def generate(self):
        print("Gerando relatório PDF")

class CSVReportGenerator(ReportGenerator):
    def generate(self):
        print("Gerando relatório CSV")

report = PDFReportGenerator()
report.generate()
