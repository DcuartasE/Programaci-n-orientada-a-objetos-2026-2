class Empleado:

    def __init__(self):
        self.horas = 48
        self.valor_hora = 5000
        self.porcentaje_retencion = 0.125

    def calcular_salario_bruto(self):
        return self.horas * self.valor_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * self.porcentaje_retencion

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()

    def mostrar(self):
        print("Salario bruto:", self.calcular_salario_bruto())
        print("Retención en la fuente:", self.calcular_retencion())
        print("Salario neto:", self.calcular_salario_neto())


class Main:

    def main(self):
        empleado = Empleado()
        empleado.mostrar()


programa = Main()
programa.main()
