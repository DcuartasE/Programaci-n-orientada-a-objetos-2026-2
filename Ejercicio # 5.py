class Operaciones:

    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 40

    def calcular(self):
        self.suma = self.suma + self.x
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y

    def mostrar(self):
        print("EL VALOR DE LA SUMA ES:", self.suma)


class Main:

    def main(self):
        operaciones = Operaciones()
        operaciones.calcular()
        operaciones.mostrar()


programa = Main()
programa.main()
