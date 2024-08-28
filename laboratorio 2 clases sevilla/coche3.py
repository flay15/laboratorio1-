class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

ferrari = Coche("Ferrari", "488 Pista")
lamborghini = Coche("Lamborghini", "Huracán EVO")

print(type(ferrari))
print(type(lamborghini))

print(ferrari.marca, ferrari.modelo)
print(lamborghini.marca, lamborghini.modelo)
