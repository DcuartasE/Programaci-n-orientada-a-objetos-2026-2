class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

    def calcular_longitud(self):
        return 2 * 3.1416 * self.radio

    def mostrar(self):
        print("Área del círculo:", self.calcular_area(), "m²")
        print("Longitud de la circunferencia:", self.calcular_longitud(), "m")


class Main:

    def main(self):
        radio = float(input("Ingrese el radio en metros: "))
        circulo = Circulo(radio)
        circulo.mostrar()


programa = Main()
programa.main()
