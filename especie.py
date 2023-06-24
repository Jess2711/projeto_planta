from planta import Planta

class Especie(Planta):
    def __init__(self, nome: str, especie: str, genero: str, quantidade_muda: int, tipo_solo: str, altura_planta: float, area_copa: float, plantio: bool = None, is_grande_porte: bool = None, tempo_adubo: str = None) -> None:
        super().__init__(quantidade_muda, altura_planta, tempo_adubo, area_copa, plantio, is_grande_porte)
        self.nome = nome
        self.especie = especie
        self.genero = genero 
        self.tipo_solo = tipo_solo
        self.lugar_planta = []

    def plantar(self):
        print('---------------')
        print('Começar plantio')
        print('---------------')

    def tempoPlantio(self):
        pass

    def __str__(self):
        return f'Nome: {self.nome}\n Especie: {self.especie}\n Genero: {self.genero}\n Tipo de Solo: {self.tipo_solo}\n' + super().__str__() 