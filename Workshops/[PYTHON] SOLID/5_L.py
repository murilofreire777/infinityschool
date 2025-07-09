class Bird:
    def fly(self):
        print("O pássaro está voando")

class Sparrow(Bird):
    def fly(self):
        print("O pardal está voando baixo")

def let_it_fly(bird: Bird):
    bird.fly()

sparrow = Sparrow()
let_it_fly(sparrow)
