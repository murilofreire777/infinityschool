
#Se criarmos uma classe Penguin que herda de Bird, mas não implementa o método fly de maneira funcional, estaremos violando o LSP.

class Penguin(Bird):
    def fly(self):
        raise Exception("Pinguins não voam")

# let_it_fly(Penguin())  # Isso causaria um erro

