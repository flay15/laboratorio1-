class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

bmw = Coche("BMW", "M5")
audi = Coche("Audi", "R8")

print(type(bmw))
print(type(audi))

print(bmw.marca, bmw.modelo)
print(audi.marca, audi.modelo)
