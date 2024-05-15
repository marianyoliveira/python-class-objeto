class Veiculo:
    def __init__(self, marca,modelo, ano):
     self.marca = marca 
     self.modelo = modelo
     self.ano = ano

    def ligar(self):
     print("Veículo ligado")

    def desligar(self):
        print("Veículo desligado"):

class Carro(Veículo):
    def __init__(self, marca. modelo, ano, numeroDePortas):
      super().__init__(marca, modelo, ano)
      self.numeroDePortas = numeroDePortas 

    def NumeroDePortas(self):
      print("O Carro possui:", self.numerodePortas)

class Moto(veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
      super().__init__(marca, modelo, ano)
      self.cilindradas = cilindradas

    def Cilindradas(self):
     print("A Moto possui: ", self.cilindradas)

veiculo = Veiculo("Toyota , Corolla, 2024, 4")
carro = Carro(" Chevrolet, Tracker, 2022, 4")
moto = Moto("Honda, twister, 2024, 293,5")

veiculo.imprimmir()
carro.imprimmir()
moto.imprimmir()