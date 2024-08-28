class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

mercedes = Coche("Mercedes","gwadon")
porsche = Coche("porsche","911 turbo S")

print(type(mercedes))
print(type(porsche))

print(mercedes.marca,mercedes.modelo)
print(porsche.marca,porsche.modelo)


