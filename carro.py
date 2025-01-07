class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


carro_jose= Carro ("Sedan", "Preto", 1999)
carro_matheus= Carro("Economico", "Cinza", 2012)
carro_farias= Carro("Ferrari", "Vermelha", 2024)

carros= [carro_jose,carro_farias,carro_matheus]

for carro in carros:
    print(f"O carro dele é {carro.modelo} na cor {carro.cor} e no ano {carro.ano}" )


