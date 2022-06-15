class Cubo:
    def __init__(self, nombre, lado):
        self.nombre = nombre
        self.lado = lado

    def cubo_nombre(self):
        return f"Nombre: {self.nombre}"

    def cubo_lado(self):
        return f"Lado: {self.lado}"

    def print_properties(self):
        print(self.cubo_nombre())
        print(self.cubo_lado())


class Esfera:
    def __init__(self, nombre, radio):
        self.nombre = nombre
        self.radio = radio

    def esfera_nombre(self):
        return self.nombre

    def esfera_radio(self):
        return f"Radio: {self.radio}"

    def print_properties(self):
        print(self.esfera_nombre())
        print(self.esfera_radio())

class Prisma_rectangular:
    def __init__(self, nombre, base, altura, profundidad):
        self.nombre = nombre
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def prisma_rectangular_nombre(self):
        return f'Nombre: {self.nombre}'

    def prisma_rectangular_bap(self):
        return f"Base: {self.base} \nAltura: {self.altura}\nProfundidad: {self.profundidad}"

    def print_properties(self):
        print(self.prisma_rectangular_nombre())
        print(self.prisma_rectangular_bap())

'''prisma1 = Prisma_rectangular("PR1", 5, 4, 9)
prisma_bap = prisma1.prisma_rectangular_bap()

print(prisma1.prisma_rectangular_nombre())
print(prisma_bap)'''
