
class Veiculo:
    def mover(self):
        print("O veículo está se movendo.")

class Carro(Veiculo):  
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

    def atualizar_ano(self, novo_ano):
        self.ano = novo_ano
        print(f"Ano atualizado para {self.ano}")

meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.mostrar_info()


meu_carro.atualizar_ano(2023)


meu_carro.mover()
