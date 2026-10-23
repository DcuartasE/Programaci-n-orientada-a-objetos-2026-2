class Familia:

    def __init__(self, juan):
        self.juan = juan
        self.alberto = (2/3) * juan
        self.ana = (4/3) * juan
        self.mama = self.juan + self.alberto + self.ana

    def mostrar_edades(self):
        print("Edad de Juan:", self.juan)
        print("Edad de Alberto:", self.alberto)
        print("Edad de Ana:", self.ana)
        print("Edad de la mamá:", self.mama)


juan = float(input("Ingrese la edad de Juan: "))

familia = Familia(juan)

familia.mostrar_edades()
