class Numero:

    def __init__(self, numero):
        self.numero = numero

    def calcular_cuadrado(self):
        return self.numero ** 2

    def calcular_cubo(self):
        return self.numero ** 3

    def mostrar(self):
        print("Cuadrado:", self.calcular_cuadrado())
        print("Cubo:", self.calcular_cubo())


class Main:

    def main(self):
        numero = float(input("Ingrese un número: "))
        n = Numero(numero)
        n.mostrar()


programa = Main()
programa.main()
