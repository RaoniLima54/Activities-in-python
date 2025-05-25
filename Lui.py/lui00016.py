class Veiculo:
    def mover(self):
        print("O veículo está se movendo.")

    def tipo(self):
        return "Veículo"

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

    def mover(self):
        print("O carro está se movendo.")

    def tipo(self):
        return "Carro"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_moto):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tipo_moto = tipo_moto  
    def mostrar_tipo(self):
        print(f"Tipo da moto: {self.tipo_moto}")

    def mover(self):
        print("A moto está se movendo.")

    def tipo(self):
        return "Moto"

meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.mostrar_info()
meu_carro.atualizar_ano(2023)
meu_carro.mover()
print("Tipo:", meu_carro.tipo())

print("\n---\n")

minha_moto = Moto("Yamaha", "MT-07", 2022, "Esportiva")
minha_moto.mostrar_tipo()
minha_moto.mover()
print("Tipo:", minha_moto.tipo())


def mostrar_tipos(lista_veiculos):
    for veiculo in lista_veiculos:
        print(veiculo.tipo())

carro1 = Carro("Honda", "Civic", 2018)
moto1 = Moto("Suzuki", "V-Strom", 2021, "Touring")
carro2 = Carro("Ford", "Focus", 2019)
moto2 = Moto("Kawasaki", "Ninja", 2020, "Esportiva")

veiculos = [carro1, moto1, carro2, moto2]

print("Tipos dos veículos na lista:")
mostrar_tipos(veiculos)
