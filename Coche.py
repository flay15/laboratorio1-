class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

gwadon = Coche("Mercedes","gwadon")
porsche = Coche("porsche","911 turbo S")

print(type(gwadon))
print(type(porsche))

print(gwadon.marca,gwadon.modelo)
print(porsche.marca,porsche.modelo)